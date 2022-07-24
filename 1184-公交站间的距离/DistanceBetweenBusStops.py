# -*- coding: utf-8 -*-
# LeetCode 1184-公交站间的距离

"""
Created on Sun Jul 24 10:48 2022

@author: _Mumu
Environment: py38
"""

from typing import List


class Solution:
    def distanceBetweenBusStops(self, distance: List[int], start: int, destination: int) -> int:
        return min(f := sum(distance[min(start, destination):max(start, destination)]), sum(distance) - f)


if __name__ == '__main__':
    s = Solution()
    print(s.distanceBetweenBusStops(distance=[1, 2, 3, 4], start=1, destination=3))
