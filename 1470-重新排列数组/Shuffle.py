# -*- coding: utf-8 -*-
# LeetCode 1470-重新排列数组

"""
Created on Mon Aug 29 11:15 2022

@author: _Mumu
Environment: py38
"""

from typing import List


class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        ys = nums[n:]
        nums[::2] = nums[:n]
        nums[1::2] = ys
        return nums
