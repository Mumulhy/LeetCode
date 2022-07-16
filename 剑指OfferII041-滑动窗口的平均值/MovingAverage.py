# -*- coding: utf-8 -*-
# LeetCode 剑指OfferII041-滑动窗口的平均值

"""
Created on Sat Jul 16 09:50 2022

@author: _Mumu
Environment: py38
"""

from collections import deque


class MovingAverage:
    def __init__(self, size: int):
        """
        Initialize your data structure here.
        """
        self.size = size
        self.k = size
        self.sum = 0
        self.nums = deque()

    def next(self, val: int) -> float:
        self.nums.append(val)
        self.sum += val
        if self.k:
            self.k -= 1
            return self.sum / (self.size - self.k)
        self.sum -= self.nums.popleft()
        return self.sum / self.size

# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)
