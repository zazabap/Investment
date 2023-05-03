# Date: 2023-04-26
# Purpose: Write some code for connect Japan Stock Market
# Website: https://www.rakuten-wallet.co.jp/service/api-leverage-exchange/

import websocket
import json

def on_message(ws, message):
    print(message)

def on_error(ws, error):
    print(error)

def on_close(ws):
    print("### closed ###")

def on_open(ws):
    print("### connected ###")
    # Subscribe to ticker channel
    subscribe_data = {
        "method": "subscribe",
        "params": {
            "channel": "ticker.btc_jpy"
        },
        "id": 1
    }
    ws.send(json.dumps(subscribe_data))

if __name__ == "__main__":
    websocket.enableTrace(True)
    ws = websocket.WebSocketApp("wss://exchange.rakuten-wallet.co.jp/ws",
                                on_message = on_message,
                                on_error = on_error,
                                on_close = on_close)
    ws.on_open = on_open
    ws.run_forever()

