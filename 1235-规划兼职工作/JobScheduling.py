# -*- coding: utf-8 -*-
# LeetCode 1235-规划兼职工作

"""
Created on Sat Oct 22 15:16 2022

@author: _Mumu
Environment: py38
"""

from bisect import bisect_right
from typing import List


class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        n = len(startTime)
        jobs = sorted(zip(endTime, startTime, profit))
        dp = [0] * (n + 1)
        for i in range(1, n + 1):
            k = bisect_right(jobs, (jobs[i - 1][1], float('inf')), hi=i)
            dp[i] = max(dp[i - 1], dp[k] + jobs[i - 1][2])
        return dp[n]


if __name__ == '__main__':
    s = Solution()
    print(s.jobScheduling(startTime=[1, 1, 1], endTime=[2, 3, 4], profit=[5, 6, 4]))
