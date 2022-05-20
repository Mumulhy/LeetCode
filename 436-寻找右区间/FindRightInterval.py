# -*- coding: utf-8 -*-
# LeetCode 436-寻找右区间

"""
Created on Fri May 20 10:30 2022

@author: _Mumu
Environment: py38
"""

from bisect import bisect_left
from typing import List


class Solution:
    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:
        n = len(intervals)
        left_points = sorted((interval[0], i) for i, interval in enumerate(intervals))
        ans = [-1] * n
        for i, (_, right_point) in enumerate(intervals):
            idx = bisect_left(left_points, (right_point, -1))
            if idx < n:
                ans[i] = left_points[idx][1]
        return ans


if __name__ == '__main__':
    s = Solution()
    print(s.findRightInterval([[1, 4], [2, 3], [3, 4]]))
