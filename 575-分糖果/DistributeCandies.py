# -*- coding: utf-8 -*-
# LeetCode 575-分糖果

"""
Created on Mon Nov 1 21:05 2021

@author: _Mumu
Environment: py38
"""

from typing import List


class Solution:
    def distributeCandies(self, candyType: List[int]) -> int:
        n = len(candyType)
        m = len(set(candyType))
        return m if 2 * m <= n else n // 2


if __name__ == '__main__':
    s = Solution()
    print(s.distributeCandies([1, 1, 2, 3]))
