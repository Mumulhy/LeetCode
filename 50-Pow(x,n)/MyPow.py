# -*- coding: utf-8 -*-
# LeetCode 50-Pow(x,n)

"""
Created on Tues Oct 12 22:14 2021

@author: _Mumu
Environment: py38
"""


class Solution:
    def myPow(self, x: float, n: int) -> float:
        if x == 0 or x == 1 or n == 1:
            return x
        if n == 0:
            return 1
        if n < 0:
            isNeg = True
            n = -n
        else:
            isNeg = False
        xPowN = 1
        while n:
            if n & 1:
                xPowN *= x
            n >>= 1
            x *= x
        if isNeg:
            return 1 / xPowN
        return xPowN


if __name__ == '__main__':
    s = Solution()
    print(s.myPow(0.5, -3))
