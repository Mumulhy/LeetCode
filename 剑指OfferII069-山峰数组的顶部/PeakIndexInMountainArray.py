# -*- coding: utf-8 -*-
# LeetCode 剑指OfferII069-山峰数组的顶部

"""
Created on Thu Oct 14 22:21 2021

@author: _Mumu
Environment: py38
"""

from typing import List


class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        left = 0
        right = len(arr) - 1
        while left < right - 1:
            mid = (left + right) // 2
            if arr[mid - 1] < arr[mid] and arr[mid] > arr[mid + 1]:
                return mid
            if arr[mid - 1] < arr[mid]:
                left = mid
            else:
                right = mid


if __name__ == '__main__':
    s = Solution()
    print(s.peakIndexInMountainArray(arr=[1, 3, 5, 4, 2]))
