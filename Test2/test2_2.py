# Student: Tanner Holtz
# Semester: Fall 2024
# Test 2
# Question 2
sales_counts = {
    "Laptop": 0,
    "Mouse": 0,
    "Keyboard": 0,
    "Monitor": 0,
    "Printer": 0
}
sales_totals = {
    "Laptop": 0.0,
    "Mouse": 0.0,
    "Keyboard": 0.0,
    "Monitor": 0.0,
    "Printer": 0.0
}

with open("test2_2.txt", 'r') as file:
    for line in file:
        line = line.strip()
        if len(line) == 0:
            continue
        sale = line.split(',')
        saleamount = float(sale[1])
        if sale[0] == "Laptop":
            sales_counts["Laptop"] += 1
            sales_totals["Laptop"] += saleamount
        elif sale[0] == "Mouse":
            sales_counts["Mouse"] += 1
            sales_totals["Mouse"] += saleamount
        elif sale[0] == "Keyboard":
            sales_counts["Keyboard"] += 1
            sales_totals["Keyboard"] += saleamount
        elif sale[0] == "Monitor":
            sales_counts["Monitor"] += 1
            sales_totals["Monitor"] += saleamount
        elif sale[0] == "Printer":
            sales_counts["Printer"] += 1
            sales_totals["Printer"] += saleamount

# Output the results
for product_name in sales_counts.keys():
    print(f"Product: {product_name}: Number of sales: {sales_counts[product_name]}, Total sales: {sales_totals[product_name]}")