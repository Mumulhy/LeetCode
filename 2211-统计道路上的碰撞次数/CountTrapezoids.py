# -*- coding: utf-8 -*-
# LeetCode 2211-统计道路上的碰撞次数

"""
Created on Thu Dec 4 22:42 2025

@author: _Mumu
Environment: py38
"""


class Solution:
    def countCollisions(self, directions: str) -> int:
        directions = directions.lstrip('L').rstrip('R')
        return len(directions) - directions.count('S')

        # has_rs = False
        # r_to_add = 0
        # ans = 0
        # for d in directions:
        #     if d == 'R':
        #         r_to_add += 1
        #         has_rs = True
        #     else:
        #         ans += r_to_add
        #         r_to_add = 0
        #         if d == 'L':
        #             if has_rs:
        #                 ans += 1
        #         else:
        #             has_rs = True
        # return ans
