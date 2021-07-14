# -*- coding: utf-8 -*-
# LeetCode 1818-绝对差值和

"""
Created on Wed Jul 14 17:28 2021

@author: _Mumu
Environment: py38
"""

from typing import List


class Solution:
    def minAbsoluteSumDiff(self, nums1: List[int], nums2: List[int]) -> int:
        n = len(nums1)
        nums1_sorted = sorted(nums1)
        abs_diffs = [abs(num1 - num2) for num1, num2 in zip(nums1, nums2)]
        max_diff = 0
        for num2, abs_diff in zip(nums2, abs_diffs):
            if num2 <= nums1_sorted[0]:
                new_diff = abs_diff - abs(nums1_sorted[0] - num2)
                if new_diff > max_diff:
                    max_diff = new_diff
                    continue
            if num2 >= nums1_sorted[n - 1]:
                new_diff = abs_diff - abs(nums1_sorted[n - 1] - num2)
                if new_diff > max_diff:
                    max_diff = new_diff
                    continue
            left = 0
            right = n - 1
            while left < right - 1:
                mid = (left + right) // 2
                if nums1_sorted[mid] > num2:
                    right = mid
                else:
                    left = mid
            new_diff = abs_diff - min(abs(nums1_sorted[left] - num2), abs(nums1_sorted[right] - num2))
            if new_diff > max_diff:
                max_diff = new_diff
        return (sum(abs_diffs) - max_diff) % 1000000007


if __name__ == '__main__':
    s = Solution()
    print(s.minAbsoluteSumDiff([1, 10, 4, 4, 2, 7], [9, 3, 5, 1, 7, 4]))
