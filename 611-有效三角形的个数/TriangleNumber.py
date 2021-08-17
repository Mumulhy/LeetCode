# -*- coding: utf-8 -*-
# LeetCode 611-有效三角形的个数

"""
Created on Wed Aug 4 15:25 2021

@author: _Mumu
Environment: py38
"""

from typing import List


class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        nums.sort()
        n = len(nums)
        triangle_num = 0
        for i in range(n):
            k = i + 2
            for j in range(i + 1, n):
                if k <= j:
                    k = j + 1
                while k < n and nums[i] + nums[j] > nums[k]:
                    k += 1
                triangle_num += k - j - 1
        return triangle_num


if __name__ == '__main__':
    s = Solution()
    print(s.triangleNumber([2, 2, 3, 4]))
