# -*- coding: utf-8 -*-
# LeetCode 812-最大三角形面积

"""
Created on Sun May 15 10:19 2022

@author: _Mumu
Environment: py38
"""

from typing import List


class Solution:
    def largestTriangleArea(self, points: List[List[int]]) -> float:
        n = len(points)
        ans = 0
        for i in range(n):
            x1, y1 = points[i]
            for j in range(i + 1, n):
                x2, y2 = points[j]
                for k in range(j + 1, n):
                    x3, y3 = points[k]
                    ans = max(ans, abs((y2 - y1) * (x3 - x1) + (y1 - y3) * (x2 - x1)))
        return ans / 2


if __name__ == '__main__':
    s = Solution()
    print(s.largestTriangleArea(points=[[0, 0], [0, 1], [1, 0], [0, 2], [2, 0]]))
