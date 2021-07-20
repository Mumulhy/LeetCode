# -*- coding: utf-8 -*-
# LeetCode 1838-最高频元素的频数

"""
Created on Mon Jul 19 21:29 2021

@author: _Mumu
Environment: py38
"""

from typing import List


class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        nums.sort()
        n = len(nums)
        left = 0
        right = 0
        max_len = 1
        diff_sum = 0
        while left < n - 1 and right < n - 1:
            right += 1
            diff_sum += (nums[right] - nums[right - 1]) * (right - left)
            while diff_sum > k:
                diff_sum -= nums[right] - nums[left]
                left += 1
            max_len = max(max_len, right - left + 1)
        return max_len


if __name__ == '__main__':
    s = Solution()
    print(s.maxFrequency(nums=[3, 9, 6], k=2))
