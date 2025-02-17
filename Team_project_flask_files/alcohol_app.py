import csv
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Path to the CSV file
CSV_FILE = 'ames_liquor_sales_2024.csv'

# Helper function to read data from the CSV file
def read_sales():
    sales = []
    try:
        with open(CSV_FILE, mode='r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                # Convert price and quantity_sold to appropriate data types
                row['name'] =  row['description']
                row['brand'] = row['vendor_name']
                row['price'] = float(row['sale'])
                row['quantity_sold'] = int(row['bottles_sold'])
                sales.append(row)
    except FileNotFoundError:
        pass  # If the file doesn't exist, return an empty list
    return sales

# Helper function to write a new sale to the CSV file
def write_sale(name, brand, price, quantity_sold):
    with open(CSV_FILE, mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([name, brand, price, quantity_sold])

@app.route('/')
def index():
    # Read sales data from the CSV file
    alcohol_list = read_sales()
    # Calculate total sales
    total_sales = sum(item['price'] * item['quantity_sold'] for item in alcohol_list)
    return render_template('display_sales.html', alcohol_list=alcohol_list, total_sales=total_sales)

@app.route('/add-sale', methods=['GET', 'POST'])
def add_sale():
    if request.method == 'POST':
        # Get data from the form
        name = request.form.get('name')
        brand = request.form.get('brand')
        try:
            price = float(request.form.get('price'))
            quantity_sold = int(request.form.get('quantity_sold'))
            # Write the new sale to the CSV file if data is valid
            if name and brand and price > 0 and quantity_sold > 0:
                write_sale(name, brand, price, quantity_sold)
        except ValueError:
            pass  # Ignore invalid input
        return redirect(url_for('index'))
    return render_template('add_sale.html')

if __name__ == '__main__':
    app.run(debug=True)
