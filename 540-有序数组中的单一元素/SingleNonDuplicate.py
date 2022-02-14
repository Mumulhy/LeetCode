# -*- coding: utf-8 -*-
# LeetCode 540-有序数组中的单一元素

"""
Created on Mon Feb 14 18:26 2022

@author: _Mumu
Environment: py38
"""

from typing import List


class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1 or nums[0] != nums[1]:
            return nums[0]
        if nums[-1] != nums[-2]:
            return nums[-1]
        left, right, mid = 0, n - 1, 0
        while left < right - 1:
            mid = (left + right) // 2
            if mid & 1 == 1:
                mid -= 1
            if nums[mid - 1] != nums[mid] and nums[mid] != nums[mid + 1]:
                return nums[mid]
            if nums[mid] == nums[mid + 1]:
                left = mid
            else:
                right = mid

        # n = len(nums)
        # if n == 1 or nums[0] != nums[1]:
        #     return nums[0]
        # if nums[-1] != nums[-2]:
        #     return nums[-1]
        # left, right, mid = 0, n - 1, 0
        # while left < right - 1:
        #     mid = (left + right) // 2
        #     if nums[mid - 1] != nums[mid] and nums[mid] != nums[mid + 1]:
        #         return nums[mid]
        #     if mid & 1 == 1:
        #         if nums[mid] == nums[mid + 1]:
        #             right = mid
        #         else:
        #             left = mid
        #     else:
        #         if nums[mid] == nums[mid + 1]:
        #             left = mid
        #         else:
        #             right = mid


if __name__ == '__main__':
    s = Solution()
    print(s.singleNonDuplicate([3, 3, 7, 7, 10, 11, 11]))
