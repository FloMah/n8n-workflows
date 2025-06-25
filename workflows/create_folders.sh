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
  "notion"
  "pdf_processing"
  "scraping"
  "semantic_search"
  "SEO"
  "calendar"
  "data_visualization"
  "email"
  "telegram"
  "slack"
  "CRM"
  "youtube"
  "vrac"
)

# Création des dossiers s’ils n’existent pas
for folder in "${folders[@]}"; do
  mkdir -p "workflows/$folder"
  echo "📁 Dossier créé : $folder"
done

echo ""
echo "✅ Tous les dossiers ont été créés avec succès."
