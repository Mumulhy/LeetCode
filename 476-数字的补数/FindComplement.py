# -*- coding: utf-8 -*-
# LeetCode 476-数字的补数

"""
Created on Mon Oct 18 15:12 2021

@author: _Mumu
Environment: py38
"""


class Solution:
    def findComplement(self, num: int) -> int:
        t = num
        n = 1
        for _ in range(5):
            t |= t >> n
            n <<= 1
        return num ^ t

        # n = 0
        # x = num
        # while x:
        #     x >>= 1
        #     n += 1
        # return num ^ (2 ** n - 1)


if __name__ == '__main__':
    s = Solution()
    print(s.findComplement(5))
