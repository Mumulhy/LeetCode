# -*- coding: utf-8 -*-
# LeetCode 1984-学生分数的最小差值

"""
Created on Fri Feb 11 21:01 2022

@author: _Mumu
Environment: py38
"""

from typing import List


class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        if k == 1:
            return 0
        nums.sort()
        ans = float('inf')
        for i in range(len(nums) - k + 1):
            ans = min(ans, nums[i + k - 1] - nums[i])
        return ans


if __name__ == '__main__':
    s = Solution()
    print(s.minimumDifference(nums=[9, 4, 1, 7], k=2))
