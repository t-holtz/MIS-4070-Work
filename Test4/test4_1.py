# test4_1.py: Flask app to compute the monthly payment for a loan.

from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def home():
    return """<html><head><title>Payment Calculator</title></head>
    <body><h1>Payment Calculator</h1>
      <form action="/compute_payment" method="POST">
        <label>Enter the loan amount:</label><input type="text" value="" name="amount"/><br/>
        <label>Enter the interest rate (0.05 for 5 percent):</label><input type="text" value="" name="interest_rate"/><br/>
        <label>Enter the number of months:</label><input type="text" value="" name="months"/><br/>
        <br/><input type="submit" value="Compute Payment" />
      </form>
    </body></html>
    """

def loan_payment(amount, interest_rate, months):
    # Get monthly_interest by dividing interest_rate by 12
    # Compute "payment" from the amount, monthly_interest, and "months"
    # Payment: amount * ( monthly_interest * (1.0 + monthly_interest) ** months ) / ( (1.0 + monthly_interest) ** months – 1.0)
    monthly_interest = interest_rate / 12.0
    return amount * ( ( monthly_interest * (1.0 + monthly_interest) ** months ) /
        ( (1.0 + monthly_interest) ** months - 1.0) )

@app.route('/compute_payment', methods=['POST'])
def compute_payment():
    # Get the "amount", "interest_rate", and "months" input values from the form and convert to float.
    # Use the loan_payment() function to compute the payment from the amount, interest_rate, and months.
    amount = float(request.form['amount'])
    interest_rate = float(request.form['interest_rate'])
    months = float(request.form['months'])
    payment = loan_payment(amount, interest_rate, months)
    # Show the amount, interest_rate, months, and payment.
    return """<html><head><title>Computed Payment</title></head>
        <body><h1>Computed Payment</h1>
        <table>
        <tr><th>Value</th><th>Amount</th></tr>
        <tr><td>Loan Amount</td><td align="right">{amount}</td></tr>
        <tr><td>Interest Rate</td><td align="right">{interest_rate}</td></tr>
        <tr><td>Months</td><td align="right">{months}</td></tr>
        <tr><td>Monthly Payment</td><td align="right">{payment:.2f}</td></tr>
        </table>
        <br/>
        <a href="/">Compute Again</a>
        </body></html>""".format(amount=amount, interest_rate=interest_rate,
                                        months=months, payment=payment)

# run the Flask app (which will launch a local webserver)
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=True)