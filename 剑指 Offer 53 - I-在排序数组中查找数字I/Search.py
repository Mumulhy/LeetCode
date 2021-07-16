# -*- coding: utf-8 -*-
# LeetCode 剑指 Offer 53 - I-在排序数组中查找数字I

"""
Created on Fri Jul 16 19:54 2021

@author: _Mumu
Environment: py38
"""

from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if target not in nums:
            return 0
        if target == nums[0] and target == nums[-1]:
            return len(nums)
        elif target == nums[0]:
            return self.findTargetRight(nums, target)
        elif target == nums[-1]:
            return len(nums) - self.findTargetLeft(nums, target) - 1
        else:
            return self.findTargetRight(nums, target) - self.findTargetLeft(nums, target) - 1

    def findTargetLeft(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1
        while left < right - 1:
            mid = (left + right) // 2
            if nums[mid] >= target:
                right = mid
            else:
                left = mid
        return left

    def findTargetRight(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1
        while left < right - 1:
            mid = (left + right) // 2
            if nums[mid] > target:
                right = mid
            else:
                left = mid
        return right

if __name__ == '__main__':
    s = Solution()
    print(s.search(nums = [1,4], target = 4))