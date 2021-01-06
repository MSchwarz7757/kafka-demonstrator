from flask import Flask, request, render_template, jsonify
# from confluent import Demonstator

app = Flask(__name__)

# create a confluent-kafka instance
# my_messages = Demonstator("172.19.0.3","9092","172.19.0.4","8081")

@app.route('/')
def index():
    """Startup event"""

    # Kafka goes here

    return render_template('index.html')

@app.route('/login', methods=['POST'])
def login():
    """Single user login event"""

    user = request.form['name']

    # my_messages.produceMessage("user",{"ID":123,"username":user},{"ID":123,"username":user})

    return render_template('user.html', user=user)

@app.route('/mouse-events')
def mouse_events():
    return render_template('user.html')

@app.route('/mouse-events', methods=['POST'])
def mouse():
  print(request.json)
  return jsonify(request.json)

@app.route('/message')
def send():
    """Multiple message sending event"""

    message = request.args.get('message', 'None', type=str)

    # my_messages.produceMessage("user",{"ID":123,"username":message},{"ID":123,"username":message})

    return jsonify(last_message=message)

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000,)
