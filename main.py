from binance.client import Client
import time

api_key = "OumRneDo6NxC2Vd02hV4oMiXDdyitJLyhNuCVR7xdXlu6PtGPhGuV31ZLFRt92YP"
api_secret = "BAcjjuqOngz4q65At9DNTBjo4Dq4he4hp5J0wMC7eyrubCHV8ijcbyChVy7fG1fp"

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