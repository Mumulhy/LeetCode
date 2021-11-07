# -*- coding: utf-8 -*-
# LeetCode 598-范围求和II

"""
Created on Sun Nov 7 23:59 2021

@author: _Mumu
Environment: py38
"""

from typing import List


class Solution:
    def maxCount(self, m: int, n: int, ops: List[List[int]]) -> int:
        minA, minB = m, n
        for a, b in ops:
            minA = min(minA, a)
            minB = min(minB, b)
        return minA * minB


if __name__ == '__main__':
    s = Solution()
    print(s.maxCount(m=3, n=3, ops=[[2, 2], [3, 3]]))
