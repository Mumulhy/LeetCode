# -*- coding: utf-8 -*-
# LeetCode 710-黑名单中的随机数

"""
Created on Sun Jun 26 12:39 2022

@author: _Mumu
Environment: py38
"""

from random import randint
from typing import List


class Solution:
    def __init__(self, n: int, blacklist: List[int]):
        m = len(blacklist)
        blacklist = set(blacklist)
        k = set(range(n - m, n))
        self.map = dict(zip(blacklist - k, k - blacklist))
        self.r = n - m - 1

    def pick(self) -> int:
        idx = randint(0, self.r)
        return self.map[idx] if idx in self.map else idx

# Your Solution object will be instantiated and called as such:
# obj = Solution(n, blacklist)
# param_1 = obj.pick()
