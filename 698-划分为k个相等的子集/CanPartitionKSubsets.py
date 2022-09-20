# -*- coding: utf-8 -*-
# LeetCode 698-划分为k个相等的子集

"""
Created on Tues Sept 20 12:36 2022

@author: _Mumu
Environment: py38
"""

from typing import List


class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        total = sum(nums)
        if total % k:
            return False
        per = total // k
        nums.sort()
        if nums[-1] > per:
            return False
        n = len(nums)
        dp = [False] * (1 << n)
        dp[0] = True
        curr_sum = [0] * (1 << n)
        for i in range(1 << n):
            if not dp[i]:
                continue
            for j in range(n):
                if curr_sum[i] + nums[j] > per:
                    break
                if i >> j & 1 == 0:
                    next = i | (1 << j)
                    if not dp[next]:
                        curr_sum[next] = (curr_sum[i] + nums[j]) % per
                        dp[next] = True
        return dp[(1 << n) - 1]
