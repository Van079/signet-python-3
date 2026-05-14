import requests
from requests.auth import HTTPBasicAuth

RPC_URL = "http://127.0.0.1:38332"
USER = "teste"
PASS = "teste"

def call_rpc(method, params=None):
    if params is None:
        params = []

    payload = {
        "jsonrpc": "1.0",
        "id": "flask",
        "method": method,
        "params": params
    }

    r = requests.post(
        RPC_URL,
        json=payload,
        auth=HTTPBasicAuth(USER, PASS),
        timeout=10
    )

    return r.json()["result"]