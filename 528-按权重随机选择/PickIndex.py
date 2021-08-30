# -*- coding: utf-8 -*-
# LeetCode 528-按权重随机选择

"""
Created on Mon Aug 30 15:21 2021

@author: _Mumu
Environment: py38
"""

from bisect import bisect_left
from itertools import accumulate
from random import randint
from typing import List


class Solution:
    def __init__(self, w: List[int]):
        self.prefixSum = list(accumulate(w))

        # self.prefixSum = [w[0]]
        # for weight in w[1:]:
        #     self.prefixSum.append(self.prefixSum[-1] + weight)

    def pickIndex(self) -> int:
        return bisect_left(self.prefixSum, randint(1, self.prefixSum[-1]))


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()

if __name__ == '__main__':
    s = Solution([1, 2, 3])
    for _ in range(20):
        print(s.pickIndex(), end=' ')
