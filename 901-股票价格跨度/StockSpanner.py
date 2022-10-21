# -*- coding: utf-8 -*-
# LeetCode 901-股票价格跨度

"""
Created on Fri Oct 21 09:56 2022

@author: _Mumu
Environment: py39
"""


class StockSpanner:
    def __init__(self):
        self.stack = [(-1, float('inf'))]
        self.idx = -1

    def next(self, price: int) -> int:
        self.idx += 1
        while self.stack[-1][1] <= price:
            self.stack.pop()
        self.stack.append((self.idx, price))
        return self.idx - self.stack[-2][0]

# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)
