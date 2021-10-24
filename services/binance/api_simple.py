import json
from websocket import WebSocketApp

SOCKET = "wss://stream.binance.com:9443/ws/"
ETH_SOCKET = SOCKET + "ethusdt@kline_1m"

def on_open(ws):
    print(":: opened connection ::")

def on_close(ws):
    print(":: closed connection ::")

def on_message(ws, raw):
#    print(":: recieved message ::")
    message = json.loads(raw)
    print("::", message)

ws = WebSocketApp(ETH_SOCKET, on_open=on_open, on_close=on_close, on_message=on_message)

print(ETH_SOCKET)
ws.run_forever()