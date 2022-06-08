# -*- coding: utf-8 -*-
# LeetCode 1037-有效的回旋镖

"""
Created on Wed Jun 8 09:57 2022

@author: _Mumu
Environment: py38
"""

from typing import List


class Solution:
    def isBoomerang(self, points: List[List[int]]) -> bool:
        (x1, y1), (x2, y2), (x3, y3) = points
        return (y3 - y1) * (x2 - x1) != (y2 - y1) * (x3 - x1)


if __name__ == '__main__':
    s = Solution()
    print(s.isBoomerang([[2, 2], [1, 1], [2, 2]]))
