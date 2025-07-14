from flask import Flask, render_template, request, redirect
from datetime import datetime
import csv
import os
import webbrowser
import threading

app = Flask(__name__)
CSV_FILE = 'pharmacy_stock.csv'

# === Medicine & Pharmacy Classes ===
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

# === CSV Load/Save ===
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
            med = Medicine(row["Name"], int(row["Stock"]), float(row["Price"]), row["Expiry"])
            pharma.add_medicine(med)

# Load data when app starts
load_from_csv()

# === Routes ===
@app.route('/')
def home():
    available = pharma.get_available()
    expired = pharma.get_expired()
    return render_template('index.html', available=available, expired=expired)

@app.route('/add', methods=['POST'])
def add_medicine():
    name = request.form['name']
    stock = int(request.form['stock'])
    price = float(request.form['price'])
    expiry = request.form['expiry']
    pharma.add_medicine(Medicine(name, stock, price, expiry))
    save_to_csv()
    return redirect('/')

@app.route('/update/<name>', methods=['GET', 'POST'])
def update_medicine(name):
    for med in pharma.medicines:
        if med.name.lower() == name.lower():
            if request.method == 'POST':
                med.price = float(request.form['price'])
                med.stock = int(request.form['stock'])
                med.expiry_date = datetime.strptime(request.form['expiry'], "%Y-%m-%d")
                save_to_csv()
                return redirect('/')
            return render_template('update.html', med=med)
    return "Medicine not found", 404

@app.route('/delete/<name>')
def delete_medicine(name):
    pharma.medicines = [med for med in pharma.medicines if med.name.lower() != name.lower()]
    save_to_csv()
    return redirect('/')

# === Start App with Auto Browser Open ===
if __name__ == '__main__':
    threading.Timer(1, lambda: webbrowser.open('http://127.0.0.1:5000')).start()
    app.run(debug=True)
