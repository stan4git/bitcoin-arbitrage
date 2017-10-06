from .observer import Observer
import json
import time
import os
from _datetime import datetime

class HistoryDumper(Observer):
    out_dir = 'history/'

    def __init__(self):
        try:
            os.mkdir(self.out_dir)
        except:
            pass

    def start_tracking_order_book(self):
        self.ob_filename = self.out_dir + 'order-book-' + \
            str(datetime.date()) + '.json'
        self.obfp = open(filename, 'w')
    
    def begin_opportunity_finder(self, depths):
        
        json.dump(depths, fp)

    def end_opportunity_finder(self):
        pass

    def opportunity(self, profit, volume, buyprice, kask, sellprice, kbid, perc, weighted_buyprice, weighted_sellprice):
        pass
