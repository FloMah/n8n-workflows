
import os
import json
from datetime import datetime

WORKFLOW_DIR = "workflows"
OUTPUT_HTML = "workflow-documentation.html"

def extract_metadata(json_path):
    with open(json_path, "r", encoding="utf-8") as f:
        try:
            data = json.load(f)
            name = data.get("name", "Unnamed Workflow")
            nodes = data.get("nodes", [])
            trigger_types = [n.get("type") for n in nodes if "trigger" in n.get("type", "").lower()]
            integrations = [n.get("parameters", {}).get("resource", "") for n in nodes if "resource" in n.get("parameters", {})]
            return {
                "name": name,
                "node_count": len(nodes),
                "trigger_types": list(set(trigger_types)),
                "integrations": list(set(filter(None, integrations))),
                "filename": os.path.basename(json_path),
            }
        except Exception as e:
            return {"name": "Invalid JSON", "node_count": 0, "trigger_types": [], "integrations": [], "filename": os.path.basename(json_path)}

def generate_html(workflows):
    html = f"""
<!DOCTYPE html>
<html lang="fr">
<head>
  <meta charset="UTF-8">
  <title>Documentation Workflows n8n</title>
  <style>
    body {{ font-family: sans-serif; background: #fff; color: #111; padding: 2rem; }}
    h1 {{ font-size: 2rem; }}
    .workflow {{ margin-bottom: 1rem; padding: 1rem; border: 1px solid #ddd; border-radius: 8px; }}
    .metadata {{ font-size: 0.9rem; color: #555; }}
    input[type="search"] {{ padding: 0.5rem; width: 100%; margin-bottom: 1.5rem; }}
  </style>
</head>
<body>
  <h1>📂 Workflows n8n — Documentation générée</h1>
  <input type="search" id="filter" placeholder="Rechercher un workflow..." oninput="filterWorkflows()"/>
  <div id="workflow-list">
"""
    for wf in workflows:
        html += f"""
    <div class="workflow">
      <strong>{wf['name']}</strong>
      <div class="metadata">
        Fichier : {wf['filename']}<br>
        Noeuds : {wf['node_count']}<br>
        Triggers : {", ".join(wf['trigger_types'])}<br>
        Intégrations : {", ".join(wf['integrations'])}
      </div>
    </div>
"""
    html += """
  </div>
  <script>
    function filterWorkflows() {
      const query = document.getElementById('filter').value.toLowerCase();
      const workflows = document.querySelectorAll('.workflow');
      workflows.forEach(el => {
        el.style.display = el.innerText.toLowerCase().includes(query) ? '' : 'none';
      });
    }
  </script>
</body>
</html>
"""
    return html

def main():
    workflows = []
    for file in os.listdir(WORKFLOW_DIR):
        if file.endswith(".json"):
            full_path = os.path.join(WORKFLOW_DIR, file)
            metadata = extract_metadata(full_path)
            workflows.append(metadata)

    html = generate_html(workflows)
    with open(OUTPUT_HTML, "w", encoding="utf-8") as f:
        f.write(html)
    print(f"Documentation générée : {OUTPUT_HTML}")

if __name__ == "__main__":
    main()
name: Generate Documentation

on:
  push:
    branches:
      - main

jobs:
  build:
    runs-on: ubuntu-latest

    steps:
      - name: Checkout code
        uses: actions/checkout@v3

      - name: Set up Python
        uses: actions/setup-python@v4
        with:
          python-version: '3.11'

      - name: Install dependencies
        run: pip install jinja2

      - name: Generate documentation
        run: python generate_documentation.py

      - name: Commit & Push generated docs
        run: |
          git config --global user.email "action@github.com"
          git config --global user.name "GitHub Action"
          git add workflow-documentation.html
          git commit -m "📚 Auto-generate workflow documentation [skip ci]" || echo "No changes to commit"
          git push
