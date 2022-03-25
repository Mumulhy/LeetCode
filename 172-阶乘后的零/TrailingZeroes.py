# -*- coding: utf-8 -*-
# LeetCode 172-阶乘后的零

"""
Created on Fri Mar 25 10:49 2022

@author: _Mumu
Environment: py38
"""


class Solution:
    def trailingZeroes(self, n: int) -> int:
        ans = 0
        x = 5
        while x <= n:
            ans += n // x
            x *= 5
        return ans


if __name__ == '__main__':
    s = Solution()
    print(s.trailingZeroes(25))
