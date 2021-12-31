# -*- coding: utf-8 -*-
# LeetCode 507-完美数

"""
Created on Fri Dec 31 12:27 2021

@author: _Mumu
Environment: py38
"""


class Solution:
    def checkPerfectNumber(self, num: int) -> bool:
        if num == 1:
            return False
        s = 1
        x = 2
        while x ** 2 < num:
            if num % x == 0:
                s += x + num // x
            if s > num:
                return False
            x += 1
        if x ** 2 == num:
            s += x
        return s == num


if __name__ == '__main__':
    s = Solution()
    print(s.checkPerfectNumber(2))
