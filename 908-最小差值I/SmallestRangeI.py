# -*- coding: utf-8 -*-
# LeetCode 908-最小差值I

"""
Created on Sat Apr 30 10:51 2022

@author: _Mumu
Environment: py38
"""

from typing import List


class Solution:
    def smallestRangeI(self, nums: List[int], k: int) -> int:
        return max(0, max(nums) - min(nums) - 2 * k)


if __name__ == '__main__':
    s = Solution()
    print(s.smallestRangeI(nums=[1, 3, 6], k=3))
