# -*- coding: utf-8 -*-
# LeetCode 1725-可以形成最大正方形的矩形数目

"""
Created on Fri Feb 4 23:00 2022

@author: _Mumu
Environment: py38
"""

from typing import List


class Solution:
    def countGoodRectangles(self, rectangles: List[List[int]]) -> int:
        ans = 0
        max_len = 0
        for rectangle in rectangles:
            curr_len = min(rectangle)
            if curr_len > max_len:
                ans = 1
                max_len = curr_len
            elif curr_len == max_len:
                ans += 1
        return ans


if __name__ == '__main__':
    s = Solution()
    print(s.countGoodRectangles([[2, 3], [3, 7], [4, 3], [3, 7]]))
