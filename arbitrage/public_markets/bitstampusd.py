import sys
from ._bitstamp import Bitstamp


class BitstampUSD(Bitstamp):
    def __init__(self):
        super(BitstampUSD, self).__init__("USD", "BTC", "USD")

if __name__ == "__main__":
    market = BitstampUSD()
    print(market.get_ticker())
