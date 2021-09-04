# -*- coding: utf-8 -*-
# LeetCode 面试题17.14-最小K个数

"""
Created on Fri Sept 3 09:58 2021

@author: _Mumu
Environment: py38
"""

from typing import List
# from heapq import heappush, heappushpop
from random import randint


class Solution:
    def smallestK(self, arr: List[int], k: int) -> List[int]:
        if k == 0:
            return []
        self.quickSelect(arr, 0, len(arr) - 1, k)
        return arr[:k]

        # kSmallest = []
        # for num in arr[:k]:
        #     heappush(kSmallest, -num)
        # for num in arr[k:]:
        #     heappushpop(kSmallest, -num)
        # return [-num for num in kSmallest]

    def quickSelect(self, arr: List[int], l: int, r: int, k: int) -> None:
        pos = self.randomizedSelect(arr, l, r)
        num = pos - l + 1
        if num > k:
            self.quickSelect(arr, l, pos - 1, k)
        elif num < k:
            self.quickSelect(arr, pos + 1, r, k - num)
        return

    def randomizedSelect(self, arr: List[int], l: int, r: int) -> int:
        i = randint(l, r)
        arr[i], arr[r] = arr[r], arr[i]
        return self.partition(arr, l, r)

    def partition(self, arr: List[int], l: int, r: int) -> int:
        pivot = arr[r]
        i = l
        for j in range(l, r):
            if arr[j] <= pivot:
                arr[i], arr[j] = arr[j], arr[i]
                i += 1
        arr[i], arr[r] = arr[r], arr[i]
        return i


if __name__ == '__main__':
    s = Solution()
    print(s.smallestK(arr=[1, 3, 5, 7, 2, 4, 6, 8], k=6))
