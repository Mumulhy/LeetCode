# -*- coding: utf-8 -*-
# LeetCode 1436-旅行终点站

"""
Created on Fri Oct 1 23:23 2021

@author: _Mumu
Environment: py38
"""

# from collections import defaultdict
from typing import List


class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        starts = {path[0] for path in paths}
        return next(path[1] for path in paths if path[1] not in starts)

        # cities = defaultdict(str)
        # for start, end in paths:
        #     cities[start] = end
        # city = paths[0][0]
        # while cities[city]:
        #     city = cities[city]
        # return city


if __name__ == '__main__':
    s = Solution()
    print(s.destCity([["A", "Z"]]))
