# -*- coding: utf-8 -*-
# LeetCode 1414-和为K的最少斐波那契数字数目

"""
Created on Thu Feb 3 22:15 2022

@author: _Mumu
Environment: py38
"""

from bisect import bisect


class Solution:
    def findMinFibonacciNumbers(self, k: int) -> int:
        feb = [1]
        x = 1
        while x <= k:
            feb.append(x)
            x = feb[-1] + feb[-2]
        step = 0
        while k:
            idx = bisect(feb, k) - 1
            k -= feb[idx]
            step += 1
        return step


if __name__ == '__main__':
    s = Solution()
    print(s.findMinFibonacciNumbers(5))
