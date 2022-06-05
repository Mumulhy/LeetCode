# -*- coding: utf-8 -*-
# LeetCode 478-在圆内随机生成点

"""
Created on Sun Jun 5 08:47 2022

@author: _Mumu
Environment: py38
"""

from random import uniform
from typing import List


class Solution:
    def __init__(self, radius: float, x_center: float, y_center: float):
        self.radius_sq = radius ** 2
        self.x_center = x_center
        self.y_center = y_center
        self.x_lim = (x_center - radius, x_center + radius)
        self.y_lim = (y_center - radius, y_center + radius)

    def randPoint(self) -> List[float]:
        x, y = uniform(*self.x_lim), uniform(*self.y_lim)
        while (x - self.x_center) ** 2 + (y - self.y_center) ** 2 > self.radius_sq:
            x, y = uniform(*self.x_lim), uniform(*self.y_lim)
        return [x, y]


# Your Solution object will be instantiated and called as such:
# obj = Solution(radius, x_center, y_center)
# param_1 = obj.randPoint()

if __name__ == '__main__':
    s = Solution(1, 0, 0)
    print(s.randPoint())
