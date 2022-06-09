# -*- coding: utf-8 -*-
# LeetCode 497-非重叠矩形中的随机点

"""
Created on Thu Jun 9 09:58 2022

@author: _Mumu
Environment: py38
"""

from bisect import bisect_left
from itertools import accumulate
from random import randint
from typing import List


class Solution:
    def __init__(self, rects: List[List[int]]):
        self.left_bottoms = [(x1, y1) for x1, y1, _, _ in rects]
        self.edges = [x2 - x1 + 1 for x1, _, x2, _ in rects]
        self.areas = list(accumulate((x2 - x1 + 1) * (y2 - y1 + 1) for x1, y1, x2, y2 in rects))

    def pick(self) -> List[int]:
        idx = randint(1, self.areas[-1])
        rect_idx = bisect_left(self.areas, idx)
        (x, y), edge = self.left_bottoms[rect_idx], self.edges[rect_idx]
        point_idx = idx - 1 if rect_idx == 0 else idx - self.areas[rect_idx - 1] - 1
        return [x + point_idx % edge, y + point_idx // edge]


# Your Solution object will be instantiated and called as such:
# obj = Solution(rects)
# param_1 = obj.pick()

if __name__ == '__main__':
    s = Solution([[-2, -2, 1, 1]])
    print(s.pick())
