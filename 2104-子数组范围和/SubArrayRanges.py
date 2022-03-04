# -*- coding: utf-8 -*-
# LeetCode 2104-子数组范围和

"""
Created on Fri Mar 4 09:22 2022

@author: _Mumu
Environment: py39
"""

from typing import List


class Solution:
    def subArrayRanges(self, nums: List[int]) -> int:
        ans = 0
        n = len(nums)
        for i in range(n - 1):
            curr_max = nums[i]
            curr_min = nums[i]
            for j in range(i + 1, n):
                curr_max = max(curr_max, nums[j])
                curr_min = min(curr_min, nums[j])
                ans += curr_max - curr_min
        return ans


if __name__ == '__main__':
    s = Solution()
    print(s.subArrayRanges([4, -2, -3, 4, 1]))
