# -*- coding: utf-8 -*-
# LeetCode 553-最优除法

"""
Created on Sun Feb 27 11:14 2022

@author: _Mumu
Environment: py38
"""

from typing import List


class Solution:
    def optimalDivision(self, nums: List[int]) -> str:
        if len(nums) > 2:
            return str(nums[0]) + '/(' + '/'.join(map(str, nums[1:])) + ')'
        if len(nums) == 1:
            return str(nums[0])
        return '/'.join(map(str, nums))


if __name__ == '__main__':
    s = Solution()
    print(s.optimalDivision([1000, 100, 10, 2]))
