from flask import request, render_template, jsonify
from app import app
import os
from app.demonstrator import Demonstrator

# create a confluent-kafka instance
app.config['BROKER_URL'] = os.environ.get("BROKER_URL")
app.config['SCHEMA_REGISTRY_URL'] = os.environ.get("SCHEMA_REGISTRY_URL")
my_messages = Demonstrator(app.config["BROKER_URL"], app.config["SCHEMA_REGISTRY_URL"])

@app.route('/')
def index():
    """Startup event"""
    # Kafka goes here

    return render_template('index.html', broker_url=app.config['BROKER_URL'], schema_url=app.config['SCHEMA_REGISTRY_URL'])

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
  return jsonify(request.json)

@app.route('/message')
def send():
    """Multiple message sending event"""

    message = request.args.get('message', 'None', type=str)

    # my_messages.produceMessage("user",{"ID":123,"username":message},{"ID":123,"username":message})

    return jsonify(last_message=message)
