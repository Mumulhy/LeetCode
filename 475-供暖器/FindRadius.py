# -*- coding: utf-8 -*-
# LeetCode 475-供暖器

"""
Created on Mon Dec 20 20:44 2021

@author: _Mumu
Environment: py38
"""

from typing import List


class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        n, m = len(houses), len(heaters)
        p1, p2 = 0, 0
        radius = 0
        houses.sort()
        heaters.sort()
        while p1 < n and p2 < m:
            if houses[p1] <= heaters[p2] or p2 == m - 1:
                radius = max(radius, abs(houses[p1] - heaters[p2]))
            else:
                while p2 < m and houses[p1] > heaters[p2]:
                    p2 += 1
                p2 -= 1
                if p2 == m - 1:
                    continue
                radius = max(radius, min(houses[p1] - heaters[p2], heaters[p2 + 1] - houses[p1]))
            p1 += 1
        return radius


if __name__ == '__main__':
    s = Solution()
    print(s.findRadius([1, 1, 1, 1, 1, 1, 999, 999, 999, 999, 999], [499, 500, 501]))
