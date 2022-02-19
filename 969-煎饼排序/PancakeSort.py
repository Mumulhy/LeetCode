# -*- coding: utf-8 -*-
# LeetCode 969-煎饼排序

"""
Created on Sat Feb 19 15:03 2022

@author: _Mumu
Environment: py38
"""

from typing import List


class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        ans = []
        for k in range(len(arr), 1, -1):
            idx = arr.index(max(arr[:k]))
            if idx == k - 1:
                continue
            arr[:idx + 1] = arr[:idx + 1][::-1]
            arr[:k] = arr[:k][::-1]
            ans.append(idx + 1)
            ans.append(k)
        return ans


if __name__ == '__main__':
    s = Solution()
    print(s.pancakeSort([1, 2, 3]))
