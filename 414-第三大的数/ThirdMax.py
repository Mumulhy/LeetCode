# -*- coding: utf-8 -*-
# LeetCode 414-第三大的数

"""
Created on Wed Oct 6 23:31 2021

@author: _Mumu
Environment: py38
"""

from heapq import heappush, heappushpop

from typing import List


class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        threeMax = []
        for num in nums:
            if len(threeMax) < 3:
                if num not in threeMax:
                    heappush(threeMax, num)
            else:
                if num > threeMax[0] and num not in threeMax:
                    heappushpop(threeMax, num)
        return threeMax[0] if len(threeMax) == 3 else max(threeMax)


if __name__ == '__main__':
    s = Solution()
    print(s.thirdMax([2, 1, 2, 3, 4, 6, 5, 8, 7, 7, 7, 7, 7, 8, 8, 8, 8, 8, 8, 8, 9]))
