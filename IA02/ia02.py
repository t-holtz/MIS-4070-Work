import csv
from collections import defaultdict

liquor_sales = defaultdict(float)
total_sales = 0.0
x = 1
with open('Iowa-Liquor-Sales-Ames-2023.csv', newline='') as csvFile:
    sales = csv.DictReader(csvFile)
    for row in sales:
        product_name = row['Item Description']
        sales_amount = float(row['Sale (Dollars)'])
        liquor_sales[product_name] += sales_amount
        total_sales += sales_amount

sorted_items = sorted(liquor_sales.items(), key=lambda x: x[1], reverse=True)

print("Item Sales in Dollars:")
for item, sales in sorted_items:
    print(f"{x}. {item}: ${sales:.2f}")
    x += 1
print(f"\nTotal Sales: ${total_sales:.2f}")