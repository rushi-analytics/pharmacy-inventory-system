# 💊 Pharmacy Inventory Management System

A simple and user-friendly web-based inventory management system for pharmacies, built with Flask and deployed on Render.

## 🌐 Live Demo

🔗 [Visit the App](https://pharmacy-inventory-system-l8ph.onrender.com)

## 🚀 Features

- Add new medicine stock with expiry and pricing.
- Update existing medicines.
- View expired vs available inventory.
- Delete outdated or incorrect entries.
- Automatically loads and saves inventory to CSV.

## 🛠️ Tech Stack

- Python (Flask)
- HTML + Jinja2 Templates
- CSV File for data storage
- Deployed on Render

## 📁 File Structure

- `app.py` - Flask app logic
- `templates/` - HTML Templates (`index.html`, `update.html`)
- `pharmacy_stock.csv` - Inventory storage
- `requirements.txt` - Python dependencies

## ⚙️ Installation

```bash
git clone https://github.com/rushi-analytics/pharmacy-inventory-system
cd pharmacy-inventory-system
pip install -r requirements.txt
python app.py

⚠️ Note: This project is intended for demonstration purposes only. It uses a CSV file for storage, which is not persistent on platforms like Render. As a result, data will not be saved permanently.
