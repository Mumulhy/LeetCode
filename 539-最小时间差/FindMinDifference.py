# -*- coding: utf-8 -*-
# LeetCode 539-最小时间差

"""
Created on Tues Jan 18 19:56 2022

@author: _Mumu
Environment: py38
"""

from typing import List


class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        minutes = set()
        for time in timePoints:
            minute = (ord(time[0]) * 10 + ord(time[1])) * 60 + ord(time[-2]) * 10 + ord(time[-1]) - 671 * ord('0')
            if minute in minutes:
                return 0
            minutes.add(minute)
        minutes = sorted(minutes)
        min_diff = 720
        for i in range(len(minutes) - 1):
            min_diff = min(min_diff, minutes[i + 1] - minutes[i])
            if min_diff == 1:
                return 1
        min_diff = min(min_diff, minutes[0] + 1440 - minutes[-1])
        return min_diff


if __name__ == '__main__':
    s = Solution()
    print(s.findMinDifference(["00:00", "23:59"]))
