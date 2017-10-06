import sys
from ._gdax import GDAX


class GDAXUSD(GDAX):
    def __init__(self):
        super(GDAXUSD, self).__init__("USD", "BTC-USD")

if __name__ == "__main__":
    market = GDAXUSD()
    print(market.get_ticker())
