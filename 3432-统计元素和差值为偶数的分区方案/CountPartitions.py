# -*- coding: utf-8 -*-
# LeetCode 3432-统计元素和差值为偶数的分区方案

"""
Created on Fri Dec 5 07:27 2025

@author: _Mumu
Environment: py38
"""

from typing import List


class Solution:
    def countPartitions(self, nums: List[int]) -> int:
        return 0 if sum(nums) % 2 else len(nums) - 1
