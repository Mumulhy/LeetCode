# -*- coding: utf-8 -*-
# LeetCode 218-天际线问题

"""
Created on Tues Jul 13 20:31 2021

@author: _Mumu
Environment: py38
"""

from typing import List
from sortedcontainers import SortedList


class Solution:
    def getSkyline(self, buildings: List[List[int]]) -> List[List[int]]:
        points = []
        for building in buildings:
            points.append([building[0], -building[2]])
            points.append([building[1], building[2]])
        points.sort()
        last_height = 0
        skyline = []
        heights = SortedList([last_height])
        for point in points:
            if point[1] < 0:
                heights.add(-point[1])
            else:
                heights.remove(point[1])
            h_max = heights[-1]
            if h_max != last_height:
                skyline.append([point[0], h_max])
                last_height = h_max
        return skyline

        # 自己写的暴力算法，当然超时了
        # x_min = buildings[0][0]
        # x_max = x_min
        # for building in buildings:
        #     if building[1] > x_max:
        #         x_max = building[1]
        # skyline = []
        # for x in range(x_min, x_max+1):
        #     height = 0
        #     for building in buildings:
        #         if building[0] <= x <= building[1] and building[2] > height:
        #             height = building[2]
        #     if skyline:
        #         if height > skyline[-1][1]:
        #             skyline.append([x, height])
        #         elif height < skyline[-1][1]:
        #             skyline.append([x-1, height])
        #     else:
        #         skyline.append([x, height])
        # skyline.append([x_max, 0])
        # return skyline

if __name__ == '__main__':
    s = Solution()
    print(s.getSkyline([[2,9,10],[3,7,15],[5,12,12],[15,20,10],[19,24,8]]))