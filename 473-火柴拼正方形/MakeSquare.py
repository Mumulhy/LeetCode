# -*- coding: utf-8 -*-
# LeetCode 473-火柴拼正方形

"""
Created on Wed Jun 1 10:29 2022

@author: _Mumu
Environment: py38
"""

from typing import List


class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        totalLen = sum(matchsticks)
        if totalLen % 4:
            return False
        tLen = totalLen // 4

        dp = [-1] * (1 << len(matchsticks))
        dp[0] = 0
        for s in range(1, len(dp)):
            for k, v in enumerate(matchsticks):
                if s & (1 << k) == 0:
                    continue
                s1 = s & ~(1 << k)
                if dp[s1] >= 0 and dp[s1] + v <= tLen:
                    dp[s] = (dp[s1] + v) % tLen
                    break
        return dp[-1] == 0


if __name__ == '__main__':
    s = Solution()
    print(s.makesquare([13, 11, 1, 8, 6, 7, 8, 8, 6, 7, 8, 9, 8]))
