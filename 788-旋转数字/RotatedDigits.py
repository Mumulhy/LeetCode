# -*- coding: utf-8 -*-
# LeetCode 788-旋转数字

"""
Created on Sun Sept 25 13:43 2022

@author: _Mumu
Environment: py38
"""

from functools import cache


class Solution:
    def rotatedDigits(self, n: int) -> int:
        check = [0, 0, 1, -1, -1, 1, 1, -1, 0, 1]
        digits = [int(digit) for digit in str(n)]

        @cache
        def dfs(pos: int, bound: bool, diff: bool) -> int:
            if pos == len(digits):
                return int(diff)

            ret = 0
            for i in range(0, (digits[pos] if bound else 9) + 1):
                if check[i] != -1:
                    ret += dfs(
                        pos + 1,
                        bound and i == digits[pos],
                        diff or check[i] == 1
                    )

            return ret

        ans = dfs(0, True, False)
        dfs.cache_clear()
        return ans
