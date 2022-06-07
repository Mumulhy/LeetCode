# -*- coding: utf-8 -*-
# LeetCode 875-爱吃香蕉的珂珂

"""
Created on Tues Jun 7 15:20 2022

@author: _Mumu
Environment: py38
"""

from math import ceil
from typing import List


class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        if len(piles) == h:
            return max(piles)
        left = ceil(sum(piles) / h)
        if sum(ceil(pile / left) for pile in piles) <= h:
            return left
        right = max(piles)
        while left < right - 1:
            mid = (left + right) // 2
            if sum(ceil(pile / mid) for pile in piles) <= h:
                right = mid
            else:
                left = mid
        return right


if __name__ == '__main__':
    s = Solution()
    print(s.minEatingSpeed(piles=[3, 6, 7, 11], h=8))
