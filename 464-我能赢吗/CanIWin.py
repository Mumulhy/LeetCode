# -*- coding: utf-8 -*-
# LeetCode 464-我能赢吗

"""
Created on Sun May 22 21:19 2022

@author: _Mumu
Environment: py38
"""

from functools import lru_cache


class Solution:
    def canIWin(self, maxChoosableInteger: int, desiredTotal: int) -> bool:
        @lru_cache(None)
        def dfs(used_nums: int, curr_total: int) -> bool:
            for i in range(maxChoosableInteger):
                if (used_nums >> i) & 1 == 0:
                    if curr_total + i + 1 >= desiredTotal or not dfs(used_nums | (1 << i), curr_total + i + 1):
                        return True
            return False

        return (1 + maxChoosableInteger) * maxChoosableInteger // 2 >= desiredTotal and dfs(0, 0)


if __name__ == '__main__':
    s = Solution()
    print(s.canIWin(10, 12))
