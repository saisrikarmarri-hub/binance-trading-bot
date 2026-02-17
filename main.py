from binance.client import Client
import time

api_key = "your_real_key"
api_secret = "your_real_secret"

client = Client(api_key, api_secret)
client.API_URL = "https://testnet.binance.vision/api"

print("AUTO BOT STARTED")

while True:

    print("Buying BTC...")
    client.order_market_buy(
        symbol='BTCUSDT',
        quantity=0.001
    )

    time.sleep(5)

    print("Selling BTC...")
    client.order_market_sell(
        symbol='BTCUSDT',
        quantity=0.001
    )

    print("Cycle Complete")


    time.sleep(10)
