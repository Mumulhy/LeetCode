# -*- coding: utf-8 -*-
# LeetCode 1217-玩筹码

"""
Created on Fri Jul 8 10:19 2022

@author: _Mumu
Environment: py38
"""

from typing import List


class Solution:
    def minCostToMoveChips(self, position: List[int]) -> int:
        odds = sum(p & 1 for p in position)
        return min(odds, len(position) - odds)


if __name__ == '__main__':
    s = Solution()
    print(s.minCostToMoveChips([1, 1000000000]))
