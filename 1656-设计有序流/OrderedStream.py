# -*- coding: utf-8 -*-
# LeetCode 1656-设计有序流

"""
Created on Tues Aug 16 09:37 2022

@author: _Mumu
Environment: py39
"""

from typing import List


class OrderedStream:
    def __init__(self, n: int):
        self.stream = [None] * (n + 1)
        self.n = n
        self.p = 1

    def insert(self, idKey: int, value: str) -> List[str]:
        self.stream[idKey] = value
        ans = []
        while self.p <= self.n and self.stream[self.p]:
            ans.append(self.stream[self.p])
            self.p += 1
        return ans

# Your OrderedStream object will be instantiated and called as such:
# obj = OrderedStream(n)
# param_1 = obj.insert(idKey,value)
