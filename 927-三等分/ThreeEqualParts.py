# -*- coding: utf-8 -*-
# LeetCode 927-三等分

"""
Created on Thu Oct 6 16:37 2022

@author: _Mumu
Environment: py38
"""

from typing import List


class Solution:
    def threeEqualParts(self, arr: List[int]) -> List[int]:
        s = sum(arr)
        if s % 3:
            return [-1, -1]
        if s == 0:
            return [0, 2]

        partial = s // 3
        first = second = third = cur = 0
        for i, x in enumerate(arr):
            if x:
                if cur == 0:
                    first = i
                elif cur == partial:
                    second = i
                elif cur == 2 * partial:
                    third = i
                cur += 1

        n = len(arr)
        length = n - third
        if first + length <= second and second + length <= third:
            i = 0
            while third + i < n:
                if arr[first + i] != arr[second + i] or arr[first + i] != arr[third + i]:
                    return [-1, -1]
                i += 1
            return [first + length - 1, second + length]
        return [-1, -1]


if __name__ == '__main__':
    s = Solution()
    print(s.threeEqualParts(arr=[1, 0, 1, 0, 1]))
