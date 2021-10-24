import json
import time
from websocket import create_connection, WebSocketConnectionClosedException

ENDPOINT = "wss://ws-feed.exchange.coinbase.com"

ws = create_connection(ENDPOINT)

ws.send(
            json.dumps(
                {
                    "type": "subscribe",
                    "product_ids": ["ETH-USD"],
                    "channels": ["ticker"],
                }
            )
        )

while True:
    result = ws.recv()
    
    msg = json.loads(result)

    print("message:", msg)
    