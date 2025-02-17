import csv

total_checking = 0.0
total_savings = 0.0

with open("accounts.csv", "r", newline='') as input_file:
    reader = csv.DictReader(input_file)
    for row in reader:
        account_type = row['type']
        account_balance = float(row['balance'])
        if account_type == "CHECKING":
            total_checking += account_balance
        else:
            total_savings += account_balance
            
print(f'Total checking balance: {total_checking}')
print(f'Total savings balance: {total_savings}')
print(f'Total balance of all accounts: {total_checking + total_savings}')