# 🤖 MyPetition Bot — https://www.mypetition.org/

**MyPetition Bot** is a Python project based on **Playwright** that automates a petition form on a website.

## 📌 How It Works

The bot is able to:

* 🌐 Automatically open a web page
* 🍪 Interact with a cookie consent window
* 📧 Detect an email address field
* ✍️ Automatically fill in the field with an email address
* 🔘 Select an option in the form
* 🖱️ Interact with a button
* 🔄 Repeat the scenario with multiple test data entries
* 🧪 Serve as a foundation for automated testing

## 🛠️ Technologies

* **Python**
* **Playwright**
* **Chromium**

## 🛠️ Installation

### Install Playwright

```bash
python -m pip install playwright
```

### Install Chromium

After installing Playwright, install the Chromium browser with:

```bash
playwright install chromium
```

## 📁 Project Structure

```text
ScriptPetition/
│
├── main.py
├── emails.json
└── README.md
```
