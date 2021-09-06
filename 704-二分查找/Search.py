# -*- coding: utf-8 -*-
# LeetCode 704-二分查找

"""
Created on Sun Sept 6 11:01 2021

@author: _Mumu
Environment: py38
"""

from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if target < nums[0] or target > nums[-1]:
            return -1
        if target == nums[0]:
            return 0
        if target == nums[-1]:
            return len(nums) - 1
        left, right = 0, len(nums) - 1
        while left < right - 1:
            mid = (left + right) // 2
            if target == nums[mid]:
                return mid
            if target < nums[mid]:
                right = mid
            else:
                left = mid
        return -1


if __name__ == '__main__':
    s = Solution()
    print(s.search(nums=[-1, 0, 3, 5, 9, 12], target=2))
