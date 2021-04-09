# -*- coding: utf-8 -*-
# LeetCode 154-寻找旋转排序数组中的最小值II

"""
Created on Fri Apr 9 23:21 2021

@author: _Mumu
Environment: py37
"""


class Solution:
    def findMin(self, nums: list) -> int:
        left = 0
        right = len(nums) - 1
        if right == 0 or nums[left] < nums[right]:
            return nums[left]
        while True:
            if right == left + 1 or right == left:
                return nums[right]
            mid = (left + right) // 2
            if nums[mid] < nums[left]:
                right = mid
            elif nums[mid] > nums[right]:
                left = mid
            else:
                if nums[left + 1] >= nums[left]:
                    left += 1
                else:
                    return nums[left + 1]
                if nums[right - 1] <= nums[right]:
                    right -= 1
                else:
                    return nums[right]


if __name__ == '__main__':
    s = Solution()
    print(s.findMin([10, 1, 10, 10, 10]))
