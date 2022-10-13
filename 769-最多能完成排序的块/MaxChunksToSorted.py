# -*- coding: utf-8 -*-
# LeetCode 769-最多能完成排序的块

"""
Created on Thu Oct 13 10:01 2022

@author: _Mumu
Environment: py39
"""

from typing import List


class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        ans = 0
        curr_max = 0
        for i, num in enumerate(arr):
            curr_max = max(curr_max, num)
            if i == curr_max:
                ans += 1
        return ans


if __name__ == '__main__':
    s = Solution()
    print(s.maxChunksToSorted([1, 0, 2, 3, 4]))
