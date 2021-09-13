# -*- coding: utf-8 -*-
# LeetCode 447-回旋镖的数量

"""
Created on Mon Sept 13 17:19 2021

@author: _Mumu
Environment: py38
"""

from collections import defaultdict
from typing import List


class Solution:
    def numberOfBoomerangs(self, points: List[List[int]]) -> int:
        n = len(points)
        if n <= 2:
            return 0
        distances = {}
        for i in range(n):
            distances[i] = defaultdict(int)
        boomerangs = 0
        for i in range(n):
            for j in range(i + 1, n):
                distance = (points[i][0] - points[j][0]) ** 2 + (points[i][1] - points[j][1]) ** 2
                distances[i][distance] += 1
                distances[j][distance] += 1
            for val in distances[i].values():
                if val >= 2:
                    boomerangs += val * (val - 1)
        return boomerangs

        # boomerangs = 0
        # for p in points:
        #     distances = defaultdict(int)
        #     for q in points:
        #         if p == q:
        #             continue
        #         distance = (p[0] - q[0]) ** 2 + (p[1] - q[1]) ** 2
        #         boomerangs += distances[distance]
        #         distances[distance] += 1
        # return boomerangs * 2

        # n = len(points)
        # if n <= 2:
        #     return 0
        # distances = {}
        # for i in range(n):
        #     distances[i] = defaultdict(int)
        # boomerangs = 0
        # for i in range(n):
        #     for j in range(i + 1, n):
        #         distance = (points[i][0] - points[j][0]) ** 2 + (points[i][1] - points[j][1]) ** 2
        #         boomerangs += distances[i][distance] + distances[j][distance]
        #         distances[i][distance] += 1
        #         distances[j][distance] += 1
        # return boomerangs * 2

        # boomerangs = 0
        # for p in points:
        #     distances = defaultdict(int)
        #     for q in points:
        #         if p == q:
        #             continue
        #         distance = (p[0] - q[0]) ** 2 + (p[1] - q[1]) ** 2
        #         distances[distance] += 1
        #     for val in distances.values():
        #         boomerangs += val * (val - 1)
        # return boomerangs


if __name__ == '__main__':
    s = Solution()
    print(s.numberOfBoomerangs(points=[[1, 1], [2, 2], [3, 3], [4, 4], [5, 5], [1, 5]]))
