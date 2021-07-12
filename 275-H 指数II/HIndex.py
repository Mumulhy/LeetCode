# -*- coding: utf-8 -*-
# LeetCode 275-H 指数II

"""
Created on Sun Jul 12 20:56 2021

@author: _Mumu
Environment: py38
"""

from typing import List


class Solution:
    def hIndex(self, citations: List[int]) -> int:
        left = 0
        right = len(citations) - 1
        if citations[left] >= right + 1:
            return right + 1
        if citations[right] == 0:
            return 0
        while left < right - 1:
            mid = (left + right) // 2
            if citations[mid] < len(citations) - mid:
                left = mid
            else:
                right = mid
        return len(citations) - right


if __name__ == '__main__':
    s = Solution()
    print(s.hIndex([1, 1, 2, 2, 2, 4, 4, 4]))
