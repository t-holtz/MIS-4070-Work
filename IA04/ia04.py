# Student: <Tanner Holtz>
# Class: MIS4070
# Semester: Fall 2024
# Assignment: ia04

from flask import Flask, render_template, request

app = Flask(__name__)

accounts = [
    {"account_num": 1000, "name": "Checking", "balance": 1000.00},
    {"account_num": 1001, "name": "Savings", "balance": 2000.00}
]
transactions = [
    {"account_num": 1000, "type": "None", "date": "10/01/2024", "description": "Initial balance", "amount": 1000.00},
    {"account_num": 1001, "type": "None", "date": "10/01/2024", "description": "Initial balance", "amount": 2000.00},
]

def find_account(num):
    """ Find the account with the given account number. """
    for account in accounts:
        if account["account_num"] == num:
            return account
    return None


@app.route('/')
def home():
    return render_template("bank-result.html",
                           transaction_list=transactions, account_list=accounts)

@app.route('/check', methods=['GET'])
def check_form():
    """ Show the check entry form to the user. """
    return render_template("bank-check.html")

@app.route('/deposit', methods=['GET'])
def deposit_form():
    """ Show the deposit entry form to the user. """
    return render_template("bank-deposit.html")

@app.route('/check', methods=['POST'])
def check_post():
    account_num = int(request.form['account_num'])
    date = request.form['date']
    description = request.form['description']
    amount = float(request.form['amount'])

    account = find_account(account_num)

    account['balance'] -= amount

    transactions.append({
        'account num': account_num,
        'type': 'Check',
        'date': date,
        'description': description,
        'amount': amount
    })

    return render_template("bank-result.html",
                           transaction_list=transactions, account_list=accounts)

@app.route('/deposit', methods=['POST'])
def deposit_post():
    if request.method == 'POST':
        account_num = int(request.form['account_num'])
        date = request.form['date']
        description = request.form['description']
        amount = float(request.form['amount'])
        print(account_num, amount)

        account = find_account(account_num)

        account['balance'] += amount

        transactions.append({
            'account_num': account_num,
            'type': 'Deposit',
            'date': date,
            'description': description,
            'amount': amount
        })
    return render_template("bank-result.html",
                           transaction_list=transactions, account_list=accounts)

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=8080)
