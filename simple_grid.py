#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import json
import math
from kumex.client import Trade
from kumex.client import Market


class Grid(object):

    def __init__(self):
        # read configuration from json file
        with open('config.json', 'r') as file:
            config = json.load(file)

        self.api_key = config['api_key']
        self.api_secret = config['api_secret']
        self.api_passphrase = config['api_passphrase']
        self.sandbox = config['is_sandbox']
        self.symbol = config['symbol']
        self.leverage = config['leverage']
        self.size = config['size']
        self.market = Market(self.api_key, self.api_secret, self.api_passphrase, is_sandbox=self.sandbox)
        self.trade = Trade(self.api_key, self.api_secret, self.api_passphrase, is_sandbox=self.sandbox)


if __name__ == '__main__':
    grid = Grid()
    ask_flag = False
    bid_flag = False
    ask_id = ''
    bid_id = ''
    while 1:
        l2_depth = grid.market.l2_order_book(grid.symbol)
        avg = math.floor((l2_depth['asks'][0][0] + l2_depth['bids'][0][0]) / 2)
        print('avg price =', avg)

        # whether ask order exists
        if ask_id:
            ask_details = grid.trade.get_order_details(ask_id)
            print('ask id = %s status = %s' % (ask_details['id'], ask_details['status']))
            if ask_details['status'] == 'done':
                ask_flag = False
            else:
                ask_flag = True

        # for ask, to the bottom
        if not ask_flag:
            ask_order = grid.trade.create_limit_order(grid.symbol, 'sell', grid.leverage, grid.size, avg + 1)
            ask_id = ask_order['orderId']
            print('create ask order id =', ask_id)
            ask_flag = True

        # whether bid order exists
        if bid_id:
            bid_details = grid.trade.get_order_details(bid_id)
            print('bid id = %s status = %s' % (bid_details['id'], bid_details['status']))
            if bid_details['status'] == 'done':
                bid_flag = False
            else:
                bid_flag = True

        # for bid, to the head
        if not bid_flag:
            bid_order = grid.trade.create_limit_order(grid.symbol, 'buy', grid.leverage, grid.size, avg)
            bid_id = bid_order['orderId']
            print('create bid order id =', bid_id)
            bid_flag = True
