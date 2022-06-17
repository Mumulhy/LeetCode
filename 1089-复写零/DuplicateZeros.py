# -*- coding: utf-8 -*-
# LeetCode 1089-复写零

"""
Created on Fri Jun 17 14:33 2022

@author: _Mumu
Environment: py38
"""

from typing import List


class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        pos = []
        for i, num in enumerate(arr):
            if num == 0:
                pos.append(i)
        for p in pos[::-1]:
            arr.insert(p, 0)
            arr.pop()
        return


if __name__ == '__main__':
    s = Solution()
    arr = [1, 2, 3]
    s.duplicateZeros(arr)
    print(arr)
