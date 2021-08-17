# -*- coding: utf-8 -*-
# LeetCode 1137-第N个泰波那契数

"""
Created on Sun Aug 8 13:35 2021

@author: _Mumu
Environment: py38
"""

class Solution:
    def tribonacci(self, n: int) -> int:
        if n == 0:
            return 0
        elif n == 1 or n == 2:
            return 1
        tribo = [0, 1, 1]
        for i in range(3, n + 1):
            tribo[i % 3] = sum(tribo)
        return tribo[n % 3]

if __name__ == '__main__':
    s = Solution()
    print(s.tribonacci(25))