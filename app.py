from flask import Flask, request, render_template, jsonify
app = Flask(__name__)

@app.route('/')
def index():
    """Startup event"""

    # Kafka goes here

    return render_template('index.html')

@app.route('/login', methods=['POST'])
def login():
    """Single user login event"""

    user = request.form['name']

    # Kafka goes here

    return render_template('user.html', user=user)

@app.route('/message')
def send():
    """Multiple message sending event"""

    message = request.args.get('message', 'None', type=str)

    # Kafka goes here

    return jsonify(last_message=message)

if __name__ == '__main__':
    app.run()