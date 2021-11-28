# -*- coding: utf-8 -*-
# LeetCode 519-随机翻转矩阵

"""
Created on Sat Nov 27 19:37 2021

@author: _Mumu
Environment: py38
"""

from random import randint
from typing import List


class Solution:
    def __init__(self, m: int, n: int):
        self.m = m
        self.n = n
        self.curr_zeros = m * n
        self.map = {}

    def flip(self) -> List[int]:
        x = randint(1, self.curr_zeros)
        idx = self.map.get(x, x)
        if x != self.curr_zeros:
            self.map[x] = self.map.get(self.curr_zeros, self.curr_zeros)
        if self.curr_zeros in self.map:
            self.map.pop(self.curr_zeros)
        self.curr_zeros -= 1
        idx -= 1
        return [idx // self.n, idx % self.n]

    def reset(self) -> None:
        self.map.clear()
        self.curr_zeros = self.m * self.n


# Your Solution object will be instantiated and called as such:
# obj = Solution(m, n)
# param_1 = obj.flip()
# obj.reset()

if __name__ == '__main__':
    s = Solution(3, 4)
    print(s.flip(), s.flip(), s.flip(), s.flip())
    print(s.flip(), s.flip(), s.flip(), s.flip())
    print(s.flip(), s.flip(), s.flip(), s.flip())
    s.reset()
    print(s.flip(), s.flip(), s.flip(), s.flip())
