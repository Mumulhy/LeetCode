# -*- coding: utf-8 -*-
# LeetCode 324-摆动排序II

"""
Created on Tues Jun 28 10:26 2022

@author: _Mumu
Environment: py38
"""

from typing import List


class Solution:
    def wiggleSort(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        arr = sorted(nums)
        j, k = (n + 1) // 2 - 1, n - 1
        for i in range(0, n, 2):
            nums[i] = arr[j]
            if i + 1 < n:
                nums[i + 1] = arr[k]
            j -= 1
            k -= 1


if __name__ == '__main__':
    s = Solution()
    arr = [1, 5, 1, 1, 6, 4]
    s.wiggleSort(arr)
    print(arr)
