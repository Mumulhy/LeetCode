# -*- coding: utf-8 -*-
# LeetCode 630-课程表III

"""
Created on Tues Dec 14 21:24 2021

@author: _Mumu
Environment: py38
"""

from heapq import heappush, heappushpop
from typing import List


class Solution:
    def scheduleCourse(self, courses: List[List[int]]) -> int:
        courses.sort(key=lambda x: x[1])
        durations = []
        duration_sum = 0
        for duration, last_day in courses:
            if duration + duration_sum <= last_day:
                heappush(durations, -duration)
                duration_sum += duration
            elif durations and -durations[0] > duration:
                duration_sum += heappushpop(durations, -duration) + duration
        return len(durations)


if __name__ == '__main__':
    s = Solution()
    print(s.scheduleCourse([[3, 2], [4, 3]]))
