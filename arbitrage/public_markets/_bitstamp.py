'''
Created on Oct 4, 2017

@author: stan4
'''

import requests
import json
from .market import Market
import bitstamp.client

class Bitstamp(Market):
    def __init__(self, currency, base, quote):
        super().__init__(currency)
        self.update_rate = 30
        self.client = bitstamp.client.Public()
        self.quote = quote
        self.base = base

    def update_depth(self):
        depth = self.client.order_book(True, self.base, self.quote)
        self.depth = self.format_depth(depth)

    def sort_and_format(self, l, reverse=False):
        l.sort(key=lambda x: float(x[0]), reverse=reverse)
        r = []
        for i in l:
            r.append({'price': float(i[0]), 'amount': float(i[1])})
        return r

    def format_depth(self, depth):
        bids = self.sort_and_format(depth['bids'], True)
        asks = self.sort_and_format(depth['asks'], False)
        return {'asks': asks, 'bids': bids}