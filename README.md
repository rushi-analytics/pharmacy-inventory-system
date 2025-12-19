# 💊 Pharmacy Inventory Management System

A simple and user-friendly **web-based Pharmacy Inventory Management System** built using **Flask**.  
The application supports **secure login**, medicine stock management, and is **deployed live on Render** for demonstration purposes.

---

## 🌐 Live Demo

🔗 **Application URL**  
https://pharmacy-inventory-system-l8ph.onrender.com/
https://pharmacy-inventory-system-l8ph.onrender.com/login

---

## 🔐 Login Credentials (Demo Access)

Use the following credentials to log in:

| Username | Password |
|---------|----------|
| admin   | admin123 |

> ⚠️ **Note**  
> The Register section is **UI-only for demonstration**.  
> Only the above admin credentials are supported.

---

## 🚀 Features Overview

| Feature | Description |
|-------|-------------|
| 🔐 Secure Login | Login-protected inventory access |
| ➕ Add Medicine | Add stock with price & expiry |
| ✏️ Update Medicine | Edit stock, price & expiry |
| 🗑 Delete Medicine | Remove incorrect entries |
| 📦 Available Inventory | View valid medicines |
| ❌ Expired Inventory | Auto-detect expired stock |
| 💾 CSV Storage | Auto save/load inventory |
| 🌐 Cloud Hosting | Deployed on Render |

---

## 🛠️ Technology Stack

| Layer | Technology |
|------|-----------|
| Backend | Python (Flask) |
| Frontend | HTML, CSS, Jinja2 |
| Auth | Flask Sessions |
| Storage | CSV File |
| Hosting | Render Cloud |

---

## 📁 Project Structure

```text
pharmacy-inventory-system/
├── app.py
├── static/
│   ├── style.css
│   └── script.js
├── templates/
│   ├── login.html
│   ├── inventory.html
│   └── update.html
├── pharmacy_stock.csv
├── requirements.txt
└── README.md
⚙️ Installation & Local Setup
bash
Copy code
git clone https://github.com/rushi-analytics/pharmacy-inventory-system.git
cd pharmacy-inventory-system
pip install -r requirements.txt
python app.py
Open browser:

cpp
Copy code
http://127.0.0.1:5000
🧪 Application Flow
Login using demo credentials

Inventory dashboard loads

Add / update / delete medicines

System auto-classifies expired items

Data is stored in CSV

⚠️ Important Notes
Project is for learning & demo purposes

CSV storage is not persistent on Render

Data may reset on redeploy

Login is hardcoded (admin-only)

🚧 Future Enhancements
Database integration (SQLite/PostgreSQL)

Password hashing

OAuth (Google / GitHub / LinkedIn)

Role-based access

Dashboard analytics

👨‍💻 Author
Rushikesh Nagapurkar
GitHub: https://github.com/rushi-analytics
