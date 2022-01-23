# -*- coding: utf-8 -*-
# LeetCode 2034-股票价格波动

"""
Created on Sun Jan 23 10:23 2022

@author: _Mumu
Environment: py38
"""

from heapq import heappush, heappop


class StockPrice:
    def __init__(self):
        self.data = {}
        self.curr_time = 0
        self.max_heap = []
        self.min_heap = []

    def update(self, timestamp: int, price: int) -> None:
        heappush(self.max_heap, (-price, timestamp))
        heappush(self.min_heap, (price, timestamp))
        self.data[timestamp] = price
        self.curr_time = max(self.curr_time, timestamp)
        return

    def current(self) -> int:
        return self.data[self.curr_time]

    def maximum(self) -> int:
        while True:
            price, timestamp = self.max_heap[0]
            if self.data[timestamp] == -price:
                return -price
            heappop(self.max_heap)

    def minimum(self) -> int:
        while True:
            price, timestamp = self.min_heap[0]
            if self.data[timestamp] == price:
                return price
            heappop(self.min_heap)

# Your StockPrice object will be instantiated and called as such:
# obj = StockPrice()
# obj.update(timestamp,price)
# param_2 = obj.current()
# param_3 = obj.maximum()
# param_4 = obj.minimum()
