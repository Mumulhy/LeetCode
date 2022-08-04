# -*- coding: utf-8 -*-
# LeetCode 1403-非递增顺序的最小子序列

"""
Created on Thu Aug 4 09:47 2022

@author: _Mumu
Environment: py38
"""

from typing import List


class Solution:
    def minSubsequence(self, nums: List[int]) -> List[int]:
        nums.sort(reverse=True)
        i = 0
        curr_sum = nums[0]
        total = sum(nums)
        while curr_sum * 2 <= total:
            i += 1
            curr_sum += nums[i]
        return nums[:i + 1]


if __name__ == '__main__':
    s = Solution()
    print(s.minSubsequence([7]))
