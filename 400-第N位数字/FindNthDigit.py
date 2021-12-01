# -*- coding: utf-8 -*-
# LeetCode 400-第N位数字

"""
Created on Tues Nov 30 18:42 2021

@author: _Mumu
Environment: py38
"""


class Solution:
    def findNthDigit(self, n: int) -> int:
        left = n
        i = 1
        curr = 9
        while left > curr:
            left -= curr
            curr //= i
            i += 1
            curr *= 10 * i
        num = curr // i // 9 + left // i
        pos = left % i
        if pos == 0:
            return (num - 1) % 10
        num //= 10 ** (i - pos)
        return num % 10


if __name__ == '__main__':
    s = Solution()
    for k in range(1, 200):
        print(s.findNthDigit(k), end='')
        if k == 9 or k == 189:
            print()
