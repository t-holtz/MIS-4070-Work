from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def home():
    return """<html><head><title>Add Numbers</title></head>
    <body><h1>Add Numbers</h1>
      <form action="/add" method="POST">
        <label>Enter first number:</label><input type="text" value="" name="first"/><br/>
        <label>Enter second number:</label><input type="text" value="" name="second"/><br/>
        <br/><input type="submit" value="Add" />
      </form>
    </body></html>
    """

@app.route('/add', methods=['POST'])
def add():
    # Get the "first" and "second" input values from the form, convert to float,
    # and show the result
    first = float(request.form['first'])
    second = float(request.form['second'])
    result = first + second
    return """<html><head><title>Added Numbers</title></head>
    <body><h1>Added Numbers</h1>
    <p>Result: {first} + {second} = {result}
    </body></html>
    """.format(first=first, second=second, result=result)

# run the Flask app (which will launch a local webserver)
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=True)