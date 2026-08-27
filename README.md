# 🤖 MyPetition Bot - https://www.mypetition.org/


MyPetition Bot est un projet Python basé sur Playwright qui automatise un formulaire de pétition sur un site web.

## 📌 Fonctionnement

Le bot est capable de :

- 🌐 Ouvrir automatiquement une page web
- 🍪 Interagir avec une fenêtre de consentement
- 📧 Détecter un champ e-mail
- ✍️ Remplir automatiquement le champ
- 🔘 Sélectionner une option du formulaire
- 🖱️ Interagir avec un bouton
- 🔄 Répéter le scénario avec plusieurs données de test
- 🧪 Servir de base à des tests automatisés

## 🛠️ Technologies

- Python
- Playwright
- Chromium

## 🛠️ Installation

Installer Playwright :

```bash
python -m pip install playwright
```
Installer Chronium :
```bash
python -m pip install chromium
```

## 📁 Structure

```text
ScriptPetition/
│
├── main.py
├── emails.json
└── README.md
