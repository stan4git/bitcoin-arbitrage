import json
import time
import os
from _datetime import datetime
import logging
from logging.handlers import TimedRotatingFileHandler

class OrderBookLogger(object):
    out_dir = 'history/'
    path = out_dir + 'order-book-history.log'
    def __init__(self):
        try:
            os.mkdir(self.out_dir)
        except:
            pass
        self.logger = logging.getLogger("OrderBookLogger")
        self.logger.setLevel(logging.INFO)
        handler = TimedRotatingFileHandler(self.path, when='h')
        self.logger.addHandler(handler)
        self.logger.propagate = False

    def log(self, msg):
        self.logger.info("%s\t%s" % (int(round(time.time() * 1000)), msg))


    