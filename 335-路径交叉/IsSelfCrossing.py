# -*- coding: utf-8 -*-
# LeetCode 335-路径交叉

"""
Created on Fri Oct 29 23:50 2021

@author: _Mumu
Environment: py38
"""

from typing import List


class Solution:
    def isSelfCrossing(self, distance: List[int]) -> bool:
        n = len(distance)
        for i in range(3, n):
            if distance[i] >= distance[i - 2] and distance[i - 1] <= distance[i - 3]:
                return True
            if i == 4 and (distance[i - 1] == distance[i - 3]
                           and distance[i] + distance[i - 4] >= distance[i - 2]):
                return True
            if i >= 5 and (distance[i - 3] - distance[i - 5] <= distance[i - 1] <= distance[i - 3]
                           and distance[i] + distance[i - 4] >= distance[i - 2] > distance[i - 4]):
                return True
        return False


if __name__ == '__main__':
    s = Solution()
    print(s.isSelfCrossing([3, 3, 3, 2, 1, 1]))
