# 🤖 MyPetition Bot — https://www.mypetition.org/

**MyPetition Bot** est un projet Python basé sur **Playwright** qui automatise un formulaire de pétition sur un site web.

## 📌 Fonctionnement

Le bot est capable de :

* 🌐 Ouvrir automatiquement une page web
* 🍪 Interagir avec une fenêtre de consentement aux cookies
* 📧 Détecter un champ d'adresse e-mail
* ✍️ Remplir automatiquement le champ avec une adresse e-mail
* 🔘 Sélectionner une option dans le formulaire
* 🖱️ Interagir avec un bouton
* 🔄 Répéter le scénario avec plusieurs données de test
* 🧪 Servir de base pour des tests automatisés

## 🛠️ Technologies

* **Python**
* **Playwright**
* **Chromium**

## 🛠️ Installation

### Installer Playwright

```bash
python -m pip install playwright
```

### Installer Chromium

Après l'installation de Playwright, installez le navigateur Chromium avec :

```bash
playwright install chromium
```

## 📁 Structure du projet

```text
ScriptPetition/
│
├── main.py
├── emails.json
└── README.md
```
