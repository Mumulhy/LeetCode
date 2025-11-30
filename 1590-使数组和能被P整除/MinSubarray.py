# -*- coding: utf-8 -*-
# LeetCode 1590-使数组和能被P整除

"""
Created on Sun Nov 30 11:24 2025

@author: _Mumu
Environment: py38
"""

from typing import List


class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        s = sum(nums)
        if s < p:
            return -1
        s_mod = s % p
        if s_mod == 0:
            return 0
        mod = 0
        idx = {0: -1}
        ans = len(nums)
        for i, num in enumerate(nums):
            mod = (mod + num) % p
            if (mod - s_mod) % p in idx:
                ans = min(ans, i - idx[(mod - s_mod) % p])
            idx[mod] = i
        return ans if ans < len(nums) else -1
