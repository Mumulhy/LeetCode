# -*- coding: utf-8 -*-
# LeetCode 3381-长度可被K整除的子数组的最大元素和

"""
Created on Thur Nov 27 21:37 2025

@author: _Mumu
Environment: py38
"""

from typing import List


class Solution:
    def maxSubarraySum(self, nums: List[int], k: int) -> int:
        if len(nums) < 2 * k:
            k_sum = sum(nums[:k])
            max_sum = k_sum
            for i in range(k, len(nums)):
                k_sum += nums[i] - nums[i - k]
                max_sum = max(max_sum, k_sum)
            return max_sum
        dp = [None] * len(nums)
        dp[k - 1] = k_sum = sum(nums[:k])
        for i in range(k, 2 * k - 1):
            dp[i] = k_sum = k_sum + nums[i] - nums[i - k]
        for i in range(2 * k - 1, len(nums)):
            k_sum += nums[i] - nums[i - k]
            dp[i] = k_sum + dp[i - k] * (dp[i - k] > 0)
        return max(dp[k - 1:])
