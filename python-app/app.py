from flask import Flask, request, render_template, jsonify
from confluent import KafkaProducer
from confluent_kafka import avro

app = Flask(__name__)

login_value = """
{
  "type": "record",
  "namespace": "vks",
  "name": "vksDemo",
  "fields": [
    {
      "name": "ID",
      "type": "long",
      "doc": "The user ID"
    },
    {
      "name": "username",
      "type": "string",
      "doc": "The user name"
    }
  ]
}
"""
login_key = """
{
  "type": "record",
  "namespace": "vks",
  "name": "vksDemo",
  "fields": [
    {
      "name": "ID",
      "type": "long",
      "doc": "The user ID"
    },
    {
      "name": "username",
      "type": "string",
      "doc": "The user name"
    }
  ]
}
"""
login_value_avro = avro.loads(login_value)
login_key_avro = avro.loads(login_key)

message_value = """
{
  "type": "record",
  "namespace": "vks",
  "name": "vksDemo",
  "fields": [
    {
      "name": "ID",
      "type": "long",
      "doc": "The user ID"
    },
    {
      "name": "message",
      "type": "string",
      "doc": "The users message"
    }
  ]
}
"""
message_key = """
{
  "type": "record",
  "namespace": "vks",
  "name": "vksDemo",
  "fields": [
    {
      "name": "ID",
      "type": "long",
      "doc": "The user ID"
    },
    {
      "name": "message",
      "type": "string",
      "doc": "The users message"
    }
  ]
}
"""
message_value_avro = avro.loads(message_value)
message_key_avro = avro.loads(message_key)

mouse_value = """
{
  "type": "record",
  "namespace": "vks",
  "name": "vksDemo",
  "fields": [
    {
      "name": "x",
      "type": "int",
      "doc": "x movement"
    },
    {
      "name": "y",
      "type": "int",
      "doc": "y mouvement"
    }
  ]
}
"""
mouse_key = """
{
  "type": "record",
  "namespace": "vks",
  "name": "vksDemo",
  "fields": [
    {
      "name": "x",
      "type": "int",
      "doc": "x movement"
    },
    {
      "name": "y",
      "type": "int",
      "doc": "y mouvement"
    }
  ]
}
"""
mouse_value_avro = avro.loads(mouse_value)
mouse_key_avro = avro.loads(mouse_key)

# create a confluent-kafka instance
ip_b = "172.21.0.4"
ip_s = "172.21.0.5"
port_b = "9092"
port_s = "8081"
login_kafka = KafkaProducer(ip_b, port_b, ip_s, port_s, login_key_avro, login_value_avro)
message_kafka = KafkaProducer(ip_b, port_b, ip_s, port_s, message_key_avro, message_value_avro)
mouse_kafka = KafkaProducer(ip_b, port_b, ip_s, port_s, mouse_key_avro, mouse_value_avro)

@app.route('/')
def index():
    """Startup event"""

    # Kafka goes here

    return render_template('index.html')

@app.route('/login', methods=['POST'])
def login():
    """Single user login event"""

    user = request.form['name']

    login_kafka.produceMessage("login", {"ID": 123456, "username": user}, {"ID": 123456, "username": user})
    return render_template('user.html', user=user)

@app.route('/mouse-events')
def mouse_events():
    return render_template('user.html')

@app.route('/mouse-events', methods=['POST'])
def mouse():
    print(request.json)

    mouse_kafka.produceMessage("mouse", request.json, request.json)
    return jsonify(request.json)

@app.route('/message')
def send():
    """Multiple message sending event"""

    message = request.args.get('message', 'None', type=str)

    message_kafka.produceMessage("message",{"ID":123456,"message":message},{"ID":123456,"message":message})

    return jsonify(last_message=message)

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000,)
