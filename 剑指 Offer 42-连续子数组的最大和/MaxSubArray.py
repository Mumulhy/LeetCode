# -*- coding: utf-8 -*-
# LeetCode 剑指 Offer 42-连续子数组的最大和

"""
Created on Sat Jul 17 20:39 2021

@author: _Mumu
Environment: py38
"""

from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        pre = 0
        max_sum = nums[0]
        for num in nums:
            pre = max(pre + num, num)
            max_sum = max(max_sum, pre)
        return max_sum


if __name__ == '__main__':
    s = Solution()
    print(s.maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4]))
