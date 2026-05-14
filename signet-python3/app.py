from flask import Flask, jsonify, render_template
from rpc import call_rpc
from zmq_listener import start_zmq
import json
import os

app = Flask(__name__)

start_zmq()

@app.route("/")
def home():
    return render_template("index.html")

# RPC via API
@app.route("/api/mempool")
def mempool():
    return jsonify(call_rpc("getmempoolinfo"))

@app.route("/api/blockchain")
def blockchain():
    return jsonify(call_rpc("getblockchaininfo"))

# ZMQ cache
@app.route("/api/block")
def block():
    path = "data/latest_block.json"

    if not os.path.exists(path):
        return jsonify({"status": "waiting"})

    with open(path) as f:
        return jsonify(json.load(f))

if __name__ == "__main__":
    app.run(debug=True)