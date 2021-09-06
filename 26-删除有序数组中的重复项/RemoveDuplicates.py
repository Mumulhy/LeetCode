# -*- coding: utf-8 -*-
# LeetCode 26-删除有序数组中的重复项

"""
Created on Sun Sept 6 19:30 2021

@author: _Mumu
Environment: py38
"""

from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums:
            return 0
        fast, slow = 1, 0
        n = len(nums)
        while fast < n:
            if nums[fast] != nums[slow]:
                slow += 1
                nums[slow] = nums[fast]
            fast += 1
        return slow + 1

        # if len(nums) <= 1:
        #     return len(nums)
        # last = nums[-1]
        # for i in range(len(nums) - 2, -1, -1):
        #     if nums[i] == last:
        #         nums.pop(i)
        #     else:
        #         last = nums[i]
        # return len(nums)


if __name__ == '__main__':
    s = Solution()
    print(s.removeDuplicates([0, 0, 1, 1, 1, 2, 2, 3, 3, 4]))
