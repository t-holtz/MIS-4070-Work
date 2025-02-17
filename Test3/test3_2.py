import sqlite3

sqlite_filename = 'test3_2.sqlite'
conn = sqlite3.connect(sqlite_filename)
c = conn.cursor()
create_table_stmt = "CREATE TABLE IF NOT EXISTS Sales (date 'TEXT', description 'TEXT', amount 'FLOAT')"
c.execute(create_table_stmt)

date = input("Enter the date of sale: ")
description = input("Enter the description of sale: ")
amount = input("Enter the amount of sale: ")

c.execute("INSERT OR IGNORE INTO Sales VALUES (?, ?, ?)", (date, description, amount))

conn.commit()

c.execute('SELECT date, description, amount FROM Sales ORDER BY date')
total_sales = 0
for row in c:
    print(row)
    total_sales += row[2]
print("Total sales: ", total_sales)
conn.close()