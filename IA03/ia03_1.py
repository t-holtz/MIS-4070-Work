# Student: Tanner Holtz
# Class: MIS4070
# Semester: Fall 2024
# Assignment: ia03

import sqlite3

file = 'booze-central-ia-2023.sqlite'

conn = sqlite3.connect(file)
c = conn.cursor()

product_name  = str(input("Enter the product name to match: "))
count = 1

c.execute("""SELECT STORE_NAME, PRODUCT_NAME, SUM(VOLUME), SUM(SALE) 
FROM booze 
WHERE PRODUCT_NAME LIKE ? 
GROUP BY PRODUCT_NAME, STORE_NAME 
ORDER BY PRODUCT_NAME, STORE_NAME""", (f'%{product_name}%',))

total = c.fetchall()

if total:
    print(f"\nVolume and Sales of products matching '{product_name}':")
    print(f"{'Store Name':<40} {'Product Name':<30} {'Total Volume':<15} {'Total Sales':<15}")
    print('-' * 90)
    for row in total:
        store_name, product_name, total_volume, total_sales = row
        print(f"{count}. {store_name:<30} {product_name:<30} {total_volume:<15} ${total_sales:<15}")
        count += 1
else:
    print("No matching products found.")

c.close()
conn.close()