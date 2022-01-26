# -*- coding: utf-8 -*-
# LeetCode 2013-检测正方形

"""
Created on Wed Jan 26 20:27 2022

@author: _Mumu
Environment: py38
"""

from typing import List


class DetectSquares:
    def __init__(self):
        self.points = {}

    def add(self, point: List[int]) -> None:
        x, y = point
        if x in self.points:
            if y in self.points[x]:
                self.points[x][y] += 1
            else:
                self.points[x][y] = 1
        else:
            self.points[x] = {y: 1}

    def count(self, point: List[int]) -> int:
        x, y = point
        if x not in self.points:
            return 0
        ans = 0
        for y1 in self.points[x]:
            if y1 != y:
                e = abs(y - y1)
                for x1 in [x - e, x + e]:
                    if x1 in self.points and y in self.points[x1] and y1 in self.points[x1]:
                        ans += self.points[x][y1] * self.points[x1][y] * self.points[x1][y1]
        return ans

# Your DetectSquares object will be instantiated and called as such:
# obj = DetectSquares()
# obj.add(point)
# param_2 = obj.count(point)
