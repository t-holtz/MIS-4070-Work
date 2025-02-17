import csv
from collections import defaultdict
x = 1

store_item_sales = defaultdict(lambda: defaultdict(float))

with open('Iowa-Liquor-Sales-Ames-2023.csv', mode='r', newline='', encoding='utf-8') as csvfile:
    sales = csv.DictReader(csvfile)

    for row in sales:
        store = row['Store Name']
        product_name = row['Item Description']
        sale_amount = float(row['Sale (Dollars)'])
        store_item_sales[store][product_name] += sale_amount

most_popular_items = {}

for store, product_name in store_item_sales.items():
    most_popular_item = max(product_name.items(), key=lambda x: x[1])
    most_popular_items[store] = most_popular_item

print("Most popular item by dollars in each store in Ames:")
for store, (product_name, sales) in most_popular_items.items():
    print(f"{x}. {store}: {product_name} - ${sales:.2f}")
    x += 1
