#!/bin/bash

# Liste des dossiers à créer
folders=(
  "form_submissions"
  "cloud_storage"
  "sms"
  "system_admin"
  "webhooks"
  "billing_invoicing"
  "llm_tools"
  "testing_debug"
  "discord"
  "telegram"
  "email"
  "youtube"
  "notion"
  "github"
  "wordpress"
  "pipedrive"
  "pdf"
  "zapier"
  "database"
  "api_integration"
  "text_analysis"
  "seo"
  "calendar"
  "data_visualization"
  "vrac"
)

# Création des dossiers
for folder in "${folders[@]}"; do
  mkdir -p "workflows/$folder"
  echo "📁 Dossier créé : workflows/$folder"
done

# Déplacement des fichiers selon mots-clés dans le nom
for file in *.json; do
  # Skip if not a regular file
  [ -f "$file" ] || continue

  lowercase_name=$(echo "$file" | tr '[:upper:]' '[:lower:]')

  # Assign dossier selon mot-clé
  case "$lowercase_name" in
    *form*|*submission*) folder="form_submissions" ;;
    *cloud*|*drive*) folder="cloud_storage" ;;
    *sms*|*twilio*) folder="sms" ;;
    *admin*|*role*) folder="system_admin" ;;
    *webhook*) folder="webhooks" ;;
    *billing*|*invoice*) folder="billing_invoicing" ;;
    *llm*|*langchain*|*mistral*|*gpt*|*openai*) folder="llm_tools" ;;
    *test*|*debug*) folder="testing_debug" ;;
    *discord*) folder="discord" ;;
    *telegram*) folder="telegram" ;;
    *email*|*mail*|*gmail*) folder="email" ;;
    *youtube*) folder="youtube" ;;
    *notion*) folder="notion" ;;
    *github*) folder="github" ;;
    *wordpress*) folder="wordpress" ;;
    *pipedrive*) folder="pipedrive" ;;
    *pdf*) folder="pdf" ;;
    *zapier*) folder="zapier" ;;
    *postgres*|*mysql*|*sql*|*database*) folder="database" ;;
    *api*|*integration*) folder="api_integration" ;;
    *scrap*|*crawl*|*scrape*) folder="scraping" ;;
*semantic*|*embed*|*embedding*|*vector*) folder="semantic_search" ;;
*clickup*|*task*|*follow-up*) folder="task_management" ;;
*notion*) folder="notion" ;;
*seo*|*keyword*) folder="SEO" ;;
*calendar*) folder="calendar" ;;
    *sentiment*|*analy*|*classify*|*summarize*) folder="text_analysis" ;;
    *seo*|*keyword*) folder="seo" ;;
    *calendar*) folder="calendar" ;;
    *chart*|*visual*|*dash*) folder="data_visualization" ;;
    *) folder="vrac" ;;
  esac

  mv "$file" "workflows/$folder/"
  echo "📦 $file → workflows/$folder/"
done

echo ""
echo "✅ Tous les fichiers JSON ont été organisés."
