from flask import Flask, jsonify, request

app = Flask(__name__)

balance = 0

@app.route('/')
def index():
    return jsonify({'balance': balance})

@app.route('/deposit')
def deposit():
    global balance
    amount = request.args.get('amount')
    if not amount or not amount.isdigit():
        return jsonify({'error': 'Invalid or missing amount parameter'}), 400
    balance += int(amount)
    return jsonify({'balance': balance})

@app.route('/withdraw')
def withdraw():
    global balance
    amount = request.args.get('amount')
    if not amount or not amount.isdigit():
        return jsonify({'error': 'Invalid or missing amount parameter'}), 400
    amount = int(amount)
    if amount > balance:
        return jsonify({'error': 'Insufficient balance', 'balance': balance}), 400
    balance -= amount
    return jsonify({'balance': balance})

if __name__ == '__main__':
    app.run(debug=True)
