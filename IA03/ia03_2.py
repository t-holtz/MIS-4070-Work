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

c.execute("""SELECT COUNTY_NAME, PRODUCT_NAME, SUM(VOLUME), SUM(SALE) 
FROM booze 
WHERE PRODUCT_NAME LIKE ? 
GROUP BY COUNTY_NAME, PRODUCT_NAME 
ORDER BY COUNTY_NAME, PRODUCT_NAME""", (f'%{product_name}%',))

total = c.fetchall()

if total:
    print(f"\nVolume and Sales matching products '{product_name}' in each county")
    print(f"{'County':<20} {'Product Name':<27} {'Total Volume':<15} {'Total Sales':<15}")
    print('-' * 90)
    for row in total:
        county_name, product_name, total_volume, total_sales = row
        print(f"{count}. {county_name:<10} {product_name:<40} {total_volume:<10} ${total_sales:<5}")
        count += 1
else:
    print("No matching products found.")

c.close()
conn.close()