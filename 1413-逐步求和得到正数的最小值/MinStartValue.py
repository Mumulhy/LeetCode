# -*- coding: utf-8 -*-
# 1413-逐步求和得到正数的最小值

"""
Created on Tues Aug 9 09:29 2022

@author: _Mumu
Environment: py39
"""

from typing import List


class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        min_pre_sum = nums[0]
        pre_sum = nums[0]
        for num in nums[1:]:
            pre_sum += num
            min_pre_sum = min(min_pre_sum, pre_sum)
        return max(1 - min_pre_sum, 1)
