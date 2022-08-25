# -*- coding: utf-8 -*-
# LeetCode 658-找到 K 个最接近的元素

"""
Created on Thu Aug 25 13:34 2022

@author: _Mumu
Environment: py38
"""

from bisect import bisect_left
from typing import List


class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        n = len(arr)
        right = bisect_left(arr, x)
        left = right - 1
        for _ in range(k):
            if left < 0:
                right += 1
            elif right >= n or x - arr[left] <= arr[right] - x:
                left -= 1
            else:
                right += 1
        return arr[left + 1:right]


if __name__ == '__main__':
    s = Solution()
    print(s.findClosestElements(arr=[1, 2, 3, 4, 5], k=4, x=2))
