# -*- coding: utf-8 -*-
# LeetCode 1051-高度检查器

"""
Created on Mon Jun 13 10:48 2022

@author: _Mumu
Environment: py38
"""

from typing import List


class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        return sum(height != expected for height, expected in zip(heights, sorted(heights)))


if __name__ == '__main__':
    s = Solution()
    print(s.heightChecker([1, 2, 3, 4, 5]))
