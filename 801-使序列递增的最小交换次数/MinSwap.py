# -*- coding: utf-8 -*-
# LeetCode 801-使序列递增的最小交换次数

"""
Created on Mon Oct 10 10:38 2022

@author: _Mumu
Environment: py38
"""

from typing import List


class Solution:
    def minSwap(self, nums1: List[int], nums2: List[int]) -> int:
        n = len(nums1)
        a, b = 0, 1
        for i in range(1, n):
            p1 = nums1[i] > nums1[i - 1] and nums2[i] > nums2[i - 1]
            p2 = nums1[i] > nums2[i - 1] and nums2[i] > nums1[i - 1]
            if p1 and p2:
                a, b = min(a, b), min(a, b) + 1
            elif p1:
                a, b = a, b + 1
            elif p2:
                a, b = b, a + 1
        return min(a, b)


if __name__ == '__main__':
    s = Solution()
    print(s.minSwap(nums1=[0, 3, 5, 8, 9], nums2=[2, 1, 4, 6, 9]))
