# -*- coding: utf-8 -*-
# LeetCode 162-寻找峰值

"""
Created on Wed Sept 15 22:56 2021

@author: _Mumu
Environment: py38
"""

from typing import List


class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        if len(nums) == 1 or nums[0] > nums[1]:
            return 0
        if nums[-1] > nums[-2]:
            return len(nums) - 1
        left = 0
        right = len(nums) - 1
        while left < right - 1:
            mid = (left + right) // 2
            if nums[mid] > nums[mid - 1] and nums[mid] > nums[mid + 1]:
                return mid
            if nums[mid] > nums[mid - 1]:
                left = mid
            else:
                right = mid
        return left


if __name__ == '__main__':
    s = Solution()
    print(s.findPeakElement(nums=[1, 2, 1]))
