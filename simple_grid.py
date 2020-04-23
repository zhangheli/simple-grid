#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import json
import math
from kumex.client import Trade
from kumex.client import Market

if __name__ == '__main__':

    # read configuration from json file
    with open('config.json', 'r') as f:
        config = json.load(f)

    api_key = config['api_key']
    api_secret = config['api_secret']
    api_passphrase = config['api_passphrase']
    symbol = config['symbol']
    leverage = config['leverage']
    size = config['size']
    sandbox = config['is_sandbox']

    # init client
    market = Market(is_sandbox=sandbox)
    trade = Trade(api_key, api_secret, api_passphrase, is_sandbox=sandbox)

    ask_flag = False
    bid_flag = False
    ask_id = ''
    bid_id = ''
    while True:
        l2_depth = market.l2_order_book(symbol)

        avg = math.floor((l2_depth['asks'][0][0] + l2_depth['bids'][0][0]) / 2)
        print('avg price =', avg)

        # whether ask order exists
        if ask_id:
            ask_details = trade.get_order_details(ask_id)
            print('ask id = %s status = %s' % (ask_details['id'], ask_details['status']))
            if ask_details['status'] == 'done':
                ask_flag = False
            else:
                ask_flag = True

        # for ask, to the bottom
        if not ask_flag:
            ask_order = trade.create_limit_order(symbol, 'sell', leverage, size, avg + 1)
            ask_id = ask_order['orderId']
            print('create ask order id =', ask_id)
            ask_flag = True

        # whether bid order exists
        if bid_id:
            bid_details = trade.get_order_details(bid_id)
            print('bid id = %s status = %s' % (bid_details['id'], bid_details['status']))
            if bid_details['status'] == 'done':
                bid_flag = False
            else:
                bid_flag = True

        # for bid, to the head
        if not bid_flag:
            bid_order = trade.create_limit_order(symbol, 'buy', leverage, size, avg)
            bid_id = bid_order['orderId']
            print('create bid order id =', bid_id)
            bid_flag = True
