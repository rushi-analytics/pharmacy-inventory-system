💊 Pharmacy Inventory Management System

A simple, user-friendly web-based Pharmacy Inventory Management System built using Flask, featuring secure login, medicine tracking, and inventory management.
The application is deployed live on Render for demonstration purposes.

🌐 Live Demo

🔗 Visit the App:
https://pharmacy-inventory-system-l8ph.onrender.com/

🔐 Login Credentials (Demo)

Use the following credentials to access the inventory dashboard:

Username: admin
Password: admin123


⚠️ Registration UI is for demonstration only. Currently, only the above admin credentials are supported.

🚀 Features

Secure login-based access to inventory

Add new medicines with:

Stock quantity

Price

Expiry date

View medicines categorized as:

✅ Available

❌ Expired

Update existing medicine details

Delete incorrect or outdated entries

Automatic CSV-based data load and save

Clean and responsive UI

Deployed live using Render

🛠️ Tech Stack

Backend: Python (Flask)

Frontend: HTML, CSS, Jinja2

Data Storage: CSV file

Deployment: Render Cloud Platform

📁 Project Structure
pharmacy-inventory-system/
├── app.py                  # Main Flask application
├── static/
│   ├── style.css           # UI styling
│   └── script.js           # UI interactions
├── templates/
│   ├── login.html          # Login & Register UI
│   ├── inventory.html      # Inventory dashboard
│   └── update.html         # Update medicine page
├── pharmacy_stock.csv      # Inventory data storage
├── requirements.txt        # Python dependencies
└── README.md               # Project documentation

⚙️ Installation & Local Setup
git clone https://github.com/rushi-analytics/pharmacy-inventory-system.git
cd pharmacy-inventory-system
pip install -r requirements.txt
python app.py


Open in browser:

http://127.0.0.1:5000

⚠️ Important Notes

This project is intended for learning and demonstration purposes only

Inventory data is stored in a CSV file

Platforms like Render do not guarantee persistent storage

Data may reset when the app restarts or redeploys

Login system is admin-only (hardcoded) for simplicity

🚧 Future Enhancements (Planned)

User registration with database (SQLite)

Password hashing & user roles

Google / GitHub OAuth login

Persistent database storage

Dashboard analytics

👨‍💻 Author

Rushikesh Nagapurkar
🔗 GitHub: https://github.com/rushi-analytics
