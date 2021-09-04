# -*- coding: utf-8 -*-
# LeetCode 剑指Offer10-I-斐波那契数列

"""
Created on Sat Sept 4 22:52 2021

@author: _Mumu
Environment: py38
"""


class Solution:
    def fib(self, n: int) -> int:
        if n <= 1:
            return n
        a = [0, 1]
        for i in range(n - 1):
            a[i & 1] = sum(a)
        return a[n & 1] % 1000000007


if __name__ == '__main__':
    s = Solution()
    print(s.fib(8))
