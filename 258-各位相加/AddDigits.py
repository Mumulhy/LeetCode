# -*- coding: utf-8 -*-
# LeetCode 258-各位相加

"""
Created on Thu Mar 3 09:24 2022

@author: _Mumu
Environment: py39
"""


class Solution:
    def addDigits(self, num: int) -> int:
        return (num - 1) % 9 + 1 if num else 0

        # while num >= 10:
        #     n = num
        #     num = 0
        #     while n > 0:
        #         num += n % 10
        #         n //= 10
        # return num


if __name__ == '__main__':
    s = Solution()
    print(s.addDigits(38))
