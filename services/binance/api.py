# To-Do:
# Open connection, wrap new subscriptions in threading or multi-processing
# Creat api endpoint to allow other programs to start thread and use data // or write to db and access there
# Enable passing arguments to ws.send to open sockets for new data
# Add ability to make trade calls
# Keep it simple
# Document
# Save to sqlite db here, with a seperate table for each sub


import json
import time
from websocket import create_connection, WebSocketConnectionClosedException

ENDPOINT = "wss://stream.binance.com:9443/ws"

ws = create_connection(ENDPOINT)

ETH_KLINE = json.dumps(
    {
        "method": "SUBSCRIBE",
        "params": [
            "ethusdt@kline_1m",
            "ethusdt@kline_5m",
            "ethusdt@kline_1h",
            "ethusdt@kline_8h",
            "ethusdt@kline_12h"
            ],
        "id": 1
                }
)

ws.send(ETH_KLINE)

while True:
    result = ws.recv()
    
    msg = json.loads(result)

    print("message:", msg)