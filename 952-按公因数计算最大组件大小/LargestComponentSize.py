# -*- coding: utf-8 -*-
# LeetCode 952-按公因数计算最大组件大小

"""
Created on Sat Jul 30 10:36 2022

@author: _Mumu
Environment: py38
"""

from collections import defaultdict
from functools import lru_cache
from typing import List


class UnionFind:
    def __init__(self, n: int):
        self.root = list(range(n))
        self.size = [1] * n
        self.part = n

    def find(self, x: int) -> int:
        if self.root[x] != x:
            self.root[x] = self.find(self.root[x])
        return self.root[x]

    def merge(self, x: int, y: int) -> None:
        x, y = self.find(x), self.find(y)
        if x == y:
            return
        if self.size[x] >= self.size[y]:
            x, y = y, x
        self.root[x] = y
        self.size[y] += self.size[x]
        self.part -= 1
        return


@lru_cache(None)
def get_prime_factor(num: int) -> set:
    if num == 1:
        return set()
    ans = set()
    i = 2
    while i ** 2 <= num:
        if num % i == 0:
            num //= i
            ans.add(i)
            ans |= get_prime_factor(num)
            return ans
        i += 1
    ans.add(num)
    return ans


class Solution:
    def largestComponentSize(self, nums: List[int]) -> int:
        dct = defaultdict(list)
        for i, num in enumerate(nums):
            for prime_factor in get_prime_factor(num):
                dct[prime_factor].append(i)
        n = len(nums)
        uf = UnionFind(n)
        for group in dct:
            m = len(dct[group])
            for j in range(1, m):
                uf.merge(dct[group][j - 1], dct[group][j])
        return max(uf.size)


if __name__ == '__main__':
    s = Solution()
    print(s.largestComponentSize([83, 99, 39, 11, 19, 30, 31]))
