# -*- coding: utf-8 -*-
# LeetCode 2016-增量元素之间的最大差值

"""
Created on Sat Feb 26 13:23 2022

@author: _Mumu
Environment: py38
"""

from typing import List


class Solution:
    def maximumDifference(self, nums: List[int]) -> int:
        curr_min = nums[0]
        ans = -1
        for num in nums[1:]:
            if num > curr_min:
                ans = max(ans, num - curr_min)
            else:
                curr_min = num
        return ans

        # n = len(nums)
        # ans = -1
        # for i in range(n - 1):
        #     for j in range(i + 1, n):
        #         if nums[i] < nums[j]:
        #             ans = max(ans, nums[j] - nums[i])
        # return ans


if __name__ == '__main__':
    s = Solution()
    print(s.maximumDifference([7, 1, 5, 4]))
