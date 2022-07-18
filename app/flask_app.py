import os
import socket
from flask import Flask, request
import logging

LOG_FORMAT = "%(levelname)s %(asctime)s - %(message)s"
logging.basicConfig(level=logging.INFO, format=LOG_FORMAT)

app = Flask(__name__)


@app.route("/", methods=['GET'])
def home():
    return "200"


@app.route("/health", methods=['GET'])
def health():
    return "service is healthy", 200


@app.route("/host_ip", methods=['GET'])
def host_ip():
    ip = socket.gethostbyname(socket.gethostname())
    return ip


port = os.getenv("PORT")
app.run(host="0.0.0.0", port=port)
