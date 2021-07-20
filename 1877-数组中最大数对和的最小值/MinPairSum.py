# -*- coding: utf-8 -*-
# LeetCode 1877-数组中最大数对和的最小值

"""
Created on Tue Jul 20 21:16 2021

@author: _Mumu
Environment: py38
"""

from typing import List


class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        nums.sort()
        max_pair_sum = nums[0] + nums[-1]
        for i in range(1, len(nums) // 2):
            now_pair_sum = nums[i] + nums[-1 - i]
            if now_pair_sum > max_pair_sum:
                max_pair_sum = now_pair_sum
        return max_pair_sum


if __name__ == '__main__':
    s = Solution()
    print(s.minPairSum([3, 5, 4, 2, 4, 6]))
