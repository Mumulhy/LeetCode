# -*- coding: utf-8 -*-
# LeetCode 396-旋转函数

"""
Created on Fri Apr 22 10:36 2022

@author: _Mumu
Environment: py38
"""

from typing import List


class Solution:
    def maxRotateFunction(self, nums: List[int]) -> int:
        n = len(nums)
        sum_nums = sum(nums)
        f = sum(i * num for i, num in enumerate(nums))
        ans = f
        for i in range(n - 1, 0, -1):
            f = f + sum_nums - n * nums[i]
            ans = max(ans, f)
        return ans


if __name__ == '__main__':
    s = Solution()
    print(s.maxRotateFunction([100]))
