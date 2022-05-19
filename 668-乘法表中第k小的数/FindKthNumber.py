# -*- coding: utf-8 -*-
# LeetCode 668-乘法表中第k小的数

"""
Created on Wed May 18 16:09 2022

@author: _Mumu
Environment: py38
"""

from bisect import bisect_left


class Solution:
    def findKthNumber(self, m: int, n: int, k: int) -> int:
        return bisect_left(range(m * n), k, key=lambda x: x // n * n + sum(x // i for i in range(x // n + 1, m + 1)))


if __name__ == '__main__':
    s = Solution()
    print(s.findKthNumber(m=3, n=3, k=5))
