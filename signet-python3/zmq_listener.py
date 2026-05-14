import zmq
import json
import threading
import time
import os

DATA_FILE = "data/latest_block.json"

def listen_zmq():
    context = zmq.Context()
    socket = context.socket(zmq.SUB)

    socket.connect("tcp://127.0.0.1:28332")
    socket.setsockopt(zmq.SUBSCRIBE, b"")

    print("🔥 ZMQ iniciado... aguardando blocos")

    while True:
        try:
            msg = socket.recv_multipart()

            topic = msg[0]
            payload = msg[1]

            data = {
                "topic": topic.decode(errors="ignore"),
                "size_bytes": len(payload),
                "timestamp": time.time()
            }

            os.makedirs("data", exist_ok=True)

            with open(DATA_FILE, "w") as f:
                json.dump(data, f, indent=2)

            print("📦 Bloco recebido:", data)

        except Exception as e:
            print("❌ Erro ZMQ:", e)

def start_zmq():
    t = threading.Thread(target=listen_zmq, daemon=True)
    t.start()