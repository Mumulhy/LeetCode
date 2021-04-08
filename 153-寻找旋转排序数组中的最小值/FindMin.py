# -*- coding: utf-8 -*-
# LeetCode 153-寻找旋转排序数组中的最小值

"""
Created on Thu Apr 8 14:42 2021

@author: _Mumu
Environment: py37
"""


class Solution:
    def findMin(self, nums: list) -> int:
        left = 0
        right = len(nums) - 1
        if nums[left] <= nums[right]:
            return nums[left]
        while True:
            if right == left + 1:
                return nums[right]
            mid = (left + right) // 2
            if nums[mid] < nums[left]:
                right = mid
            else:
                left = mid


if __name__ == '__main__':
    s = Solution()
    print(s.findMin([11, 13, 15, 17]))
