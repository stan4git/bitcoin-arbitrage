'''
Created on Oct 5, 2017

@author: stan4
'''

import sys
from ._poloniex import Poloniex


class PoloniexUSD(Poloniex):
    def __init__(self):
        super(PoloniexUSD, self).__init__("USD", "USDT_BTC")

if __name__ == "__main__":
    market = BitstampUSD()
    print(market.get_ticker())
