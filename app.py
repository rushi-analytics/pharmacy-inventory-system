from flask import Flask, render_template, request, redirect, session, url_for
from datetime import datetime
import csv
import os

app = Flask(__name__)
app.secret_key = "secret123"   # change later

CSV_FILE = 'pharmacy_stock.csv'

# =========================
# Medicine & Pharmacy
# =========================
class Medicine:
    def __init__(self, name, stock, price, expiry):
        self.name = name
        self.stock = stock
        self.price = price
        self.expiry_date = datetime.strptime(expiry, "%Y-%m-%d")

    def is_expired(self):
        return datetime.now() > self.expiry_date


class Pharmacy:
    def __init__(self):
        self.medicines = []

    def add_medicine(self, med):
        self.medicines.append(med)

    def get_available(self):
        return [m for m in self.medicines if not m.is_expired()]

    def get_expired(self):
        return [m for m in self.medicines if m.is_expired()]


pharma = Pharmacy()

# =========================
# CSV Load / Save
# =========================
def save_to_csv():
    with open(CSV_FILE, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["Name", "Stock", "Price", "Expiry"])
        for med in pharma.medicines:
            writer.writerow([
                med.name,
                med.stock,
                med.price,
                med.expiry_date.strftime("%Y-%m-%d")
            ])

def load_from_csv():
    if not os.path.exists(CSV_FILE):
        return
    with open(CSV_FILE, mode='r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            med = Medicine(
                row["Name"],
                int(row["Stock"]),
                float(row["Price"]),
                row["Expiry"]
            )
            pharma.add_medicine(med)

# Load data on startup
load_from_csv()

# =========================
# ROUTES
# =========================

# ROOT → decide where to go
@app.route('/')
def home():
    if "user" in session:
        return redirect(url_for("inventory"))
    return redirect(url_for("login"))

# LOGIN
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')

        # TEMP LOGIN (can replace with DB / OAuth later)
        if username == 'admin' and password == 'admin123':
            session['user'] = username
            return redirect(url_for('inventory'))
        else:
            return render_template('login.html', error="Invalid credentials")

    return render_template('login.html')

# LOGOUT
@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('login'))

# INVENTORY (PROTECTED)
@app.route('/inventory')
def inventory():
    if "user" not in session:
        return redirect(url_for("login"))

    available = pharma.get_available()
    expired = pharma.get_expired()
    return render_template(
        'inventory.html',
        available=available,
        expired=expired
    )

# ADD MEDICINE (PROTECTED)
@app.route('/add', methods=['POST'])
def add_medicine():
    if "user" not in session:
        return redirect(url_for("login"))

    name = request.form['name']
    stock = int(request.form['stock'])
    price = float(request.form['price'])
    expiry = request.form['expiry']

    pharma.add_medicine(Medicine(name, stock, price, expiry))
    save_to_csv()
    return redirect(url_for('inventory'))

# UPDATE MEDICINE (PROTECTED)
@app.route('/update/<name>', methods=['GET', 'POST'])
def update_medicine(name):
    if "user" not in session:
        return redirect(url_for("login"))

    for med in pharma.medicines:
        if med.name.lower() == name.lower():
            if request.method == 'POST':
                med.price = float(request.form['price'])
                med.stock = int(request.form['stock'])
                med.expiry_date = datetime.strptime(
                    request.form['expiry'], "%Y-%m-%d"
                )
                save_to_csv()
                return redirect(url_for('inventory'))

            return render_template('update.html', med=med)

    return "Medicine not found", 404

# DELETE MEDICINE (PROTECTED)
@app.route('/delete/<name>')
def delete_medicine(name):
    if "user" not in session:
        return redirect(url_for("login"))

    pharma.medicines = [
        med for med in pharma.medicines
        if med.name.lower() != name.lower()
    ]
    save_to_csv()
    return redirect(url_for('inventory'))

# =========================
# START APP
# =========================
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000, debug=True)
