# -*- coding: utf-8 -*-
# LeetCode 9-回文数

"""
Created on Fri Jul 9 21:46 2021

@author: _Mumu
Environment: py38
"""


class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        if x == 0:
            return True
        if x % 10 == 0:
            return False
        y = 0
        while x > y:
            y = y * 10 + x % 10
            x //= 10
        if x == y or y // 10 == x:
            return True
        else:
            return False


if __name__ == '__main__':
    s = Solution()
    print(s.isPalindrome(1233212))
