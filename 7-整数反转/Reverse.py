# -*- coding: utf-8 -*-
# LeetCode 7-整数反转

"""
Created on Fri Jul 4 23:23 2021

@author: _Mumu
Environment: py38
"""


class Solution:
    def reverse(self, x: int) -> int:
        if x >= 0:
            r = int(str(x)[::-1])
        else:
            r = - int(str(x)[1:][::-1])
        if - 2 ** 31 <= r < 2 ** 31:
            return r
        else:
            return 0


if __name__ == '__main__':
    s = Solution()
    print(s.reverse(-12345))
