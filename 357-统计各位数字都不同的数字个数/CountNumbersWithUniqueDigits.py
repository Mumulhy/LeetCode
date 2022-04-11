# -*- coding: utf-8 -*-
# LeetCode 357-统计各位数字都不同的数字个数

"""
Created on Mon Apr 11 12:06 2022

@author: _Mumu
Environment: py38
"""


class Solution:
    def countNumbersWithUniqueDigits(self, n: int) -> int:
        ans = 1
        x = 9
        k = 9
        for _ in range(n):
            ans += x
            x *= k
            k -= 1
        return ans


if __name__ == '__main__':
    s = Solution()
    print(s.countNumbersWithUniqueDigits(3))
