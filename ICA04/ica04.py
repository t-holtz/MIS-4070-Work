import csv

# Initialize the dictionary of product names and total sales
sales_by_product_name = {}

# Process rows: date (column 0), product name (column 1), sale (column 2)
with open('ica04.csv', newline='')as csvfile:
    sales = csv.DictReader(csvfile)
    for row in sales:
        product_name = row['product']
        total_sales = float(row['sale'])
        if product_name not in sales_by_product_name:
            sales_by_product_name[product_name] = 0.0
        sales_by_product_name[product_name] += total_sales

# Print sorted by total sales in reverse order
for product_name, total_sales in sorted(sales_by_product_name.items(), key=lambda x: x[1], reverse=True):
    print(f"{product_name:40s} {total_sales:10.2f}")