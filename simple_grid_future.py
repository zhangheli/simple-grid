#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import json
import logging
import time
from concurrent.futures import ThreadPoolExecutor, wait, ALL_COMPLETED
from decimal import Decimal
from kumex.client import Trade
from kumex.client import Market


def log_setting():
    logging.basicConfig(filename='log.log',
                        format='%(asctime)s - %(levelname)s - %(module)s - %(lineno)d:  %(message)s',
                        datefmt='%Y-%m-%d %H:%M:%S %p',
                        level=logging.INFO)


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
        self.depth = config['depth']
        self.market = Market(self.api_key, self.api_secret, self.api_passphrase, is_sandbox=self.sandbox)
        self.trade = Trade(self.api_key, self.api_secret, self.api_passphrase, is_sandbox=self.sandbox)

        self.tick_size = 0
        self.best_ask = 0
        self.best_bid = 0
        self.diff = 0
        self.max_ask = 0
        self.max_bid = 0
        self.ask_list = {}
        self.bid_list = {}

    def get_symbol(self):
        try:
            symbol = self.market.get_contract_detail(self.symbol)
            self.tick_size = Decimal(symbol['tickSize']).quantize(Decimal("0.00"))
            self.diff = Decimal(self.tick_size * self.depth).quantize(Decimal("0.00"))

            logging.info('tick_size = %s' % self.tick_size)
        except Exception as e:
            logging.error(e)
            return

    def get_market_price(self):
        try:
            m = self.market.get_ticker(self.symbol)
            self.best_ask = Decimal(m['bestAskPrice'])
            self.max_ask = Decimal(self.best_ask + self.diff).quantize(Decimal("0.00"))
            self.best_bid = Decimal(m['bestBidPrice'])
            self.max_bid = Decimal(self.best_bid - self.diff).quantize(Decimal("0.00"))

            logging.debug('best_ask = %s' % self.best_ask)
            logging.debug('best_bid = %s' % self.best_bid)
        except Exception as e:
            logging.error(e)

    def cancel_order(self, order_id, side):
        try:
            oi = self.trade.get_order_details(order_id)
            if oi['isActive']:
                self.trade.cancel_order(order_id)

            if side == 'sell':
                del self.ask_list[order_id]
            elif side == 'buy':
                del self.bid_list[order_id]
        except Exception as e:
            logging.error('该订单状态不可撤回 side = %s, order_id = %s' % (side, order_id))
            logging.error(e)

    def ask_maker(self, p):
        try:
            price = int(p * 100) / 100
            ask = self.trade.create_limit_order(self.symbol, 'sell', self.leverage, self.size, float(price))
            logging.debug('当前盘口价格 = %s,在合约 %s 以数量= %s,价格= %s,创建了卖单,卖单ID = %s' %
                          (self.best_ask, self.symbol, self.size, float(price), ask['orderId']))
            self.ask_list[ask['orderId']] = {
                'price': p
            }
        except Exception as e:
            logging.error(e)

    def bid_maker(self, p):
        try:
            price = int(p * 100) / 100
            bid = self.trade.create_limit_order(self.symbol, 'buy', self.leverage, self.size, float(price))
            logging.debug('当前盘口价格 = %s,在合约 %s 以数量= %s,价格= %s,创建了买单,卖单ID = %s' %
                          (self.best_bid, self.symbol, self.size, float(price), bid['orderId']))
            self.bid_list[bid['orderId']] = {
                'price': p
            }
        except Exception as e:
            logging.error(e)


if __name__ == '__main__':
    log_setting()
    grid = Grid()
    grid.get_symbol()
    executor = ThreadPoolExecutor(max_workers=5)
    all_task = []
    while grid.tick_size > 0:
        grid.get_market_price()
        if grid.best_bid <= 0 or grid.best_ask <= 0:
            logging.error('best_bid or best_ask error')
            time.sleep(5)
            continue

        for k, v in (grid.ask_list.items()):
            if v['price'] < grid.best_ask or v['price'] >= grid.max_ask:
                task = executor.submit(grid.cancel_order, k, 'sell')
                all_task.append(task)
        wait(all_task, return_when=ALL_COMPLETED)
        all_task.clear()

        for k, v in (grid.bid_list.items()):
            if v['price'] > grid.best_bid or v['price'] <= grid.max_bid:
                task = executor.submit(grid.cancel_order, k, 'buy')
                all_task.append(task)
        wait(all_task, return_when=ALL_COMPLETED)
        all_task.clear()

        ask_price = grid.best_ask
        bid_price = grid.best_bid
        for i in range(0, grid.depth):
            ask_price = Decimal(grid.best_ask + grid.tick_size * Decimal(i)).quantize(Decimal("0.00"))
            flag = 0
            for k, v in (grid.ask_list.items()):
                if ask_price == v['price']:
                    flag = 1
            if flag == 0:
                task = executor.submit(grid.ask_maker, ask_price)
                all_task.append(task)
        wait(all_task, return_when=ALL_COMPLETED)
        all_task.clear()

        for i in range(0, grid.depth):
            bid_price = Decimal(grid.best_bid - grid.tick_size * Decimal(i)).quantize(Decimal("0.00"))
            flag = 0
            for k, v in (grid.bid_list.items()):
                if bid_price == v['price']:
                    flag = 1
            if flag == 0:
                task = executor.submit(grid.bid_maker, bid_price)
                all_task.append(task)
        wait(all_task, return_when=ALL_COMPLETED)
        all_task.clear()
