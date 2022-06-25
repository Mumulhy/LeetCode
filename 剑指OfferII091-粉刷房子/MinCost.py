# -*- coding: utf-8 -*-
# LeetCode 剑指OfferII091-粉刷房子

"""
Created on Sat Jun 25 12:24 2022

@author: _Mumu
Environment: py38
"""

from typing import List


class Solution:
    def minCost(self, costs: List[List[int]]) -> int:
        dp = costs[0]
        for i in range(1, len(costs)):
            dp = [costs[i][j] + min(dp[(j + 1) % 3], dp[(j + 2) % 3]) for j in range(3)]
        return min(dp)


if __name__ == '__main__':
    s = Solution()
    print(s.minCost([[17, 2, 17], [16, 16, 5], [14, 3, 19]]))
