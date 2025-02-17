import sqlite3

sqlite_file = 'bank.sqlite'

conn = sqlite3.connect(sqlite_file)
conn.isolation_level = None

cur = conn.cursor()

# Initialize accounts
cur.execute("CREATE TABLE IF NOT EXISTS bank (AccountNum 'INTEGER' PRIMARY KEY AUTOINCREMENT, Name 'TEXT', Balance 'FLOAT')")
cur.execute("INSERT OR IGNORE INTO bank VALUES (?, ?, ?)", (1000, "Checking", 1000.00))
cur.execute("INSERT OR IGNORE INTO bank VALUES (?, ?, ?)", (1001, "Savings", 2000.00))
conn.commit()

def show_accounts():
    cur.execute("SELECT * FROM bank ORDER BY AccountNum")
    print(f"Acct Description                  Balance")
    for row in cur:
        print(f"{row[0]:4d} {row[1]:25s} {row[2]: 10.2f}")

done = False
while not done:
    show_accounts()
    command = input("Enter command D)eposit, W)ithdraw, or Q)uit: ")
    command = command.upper()
    if command == "D":
        account_number = int(input("Enter account number: "))
        deposit = float(input("Enter amount to deposit: "))
        cur.execute("UPDATE bank SET Balance = Balance + ? WHERE AccountNum = ?", (deposit, account_number))
        conn.commit()
    elif command == "W":
        account_number = int(input("Enter account number: "))
        withdraw = float(input("Enter amount to withdraw: "))
        cur.execute("UPDATE bank SET Balance = Balance - ? WHERE AccountNum = ?", (withdraw, account_number))
        conn.commit()
    elif command == "Q":
        done = True
    else:
        print("What?")