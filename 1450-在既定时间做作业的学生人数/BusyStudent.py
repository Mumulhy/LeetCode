# -*- coding: utf-8 -*-
# LeetCode 1450-在既定时间做作业的学生人数

"""
Created on Fri Aug 19 10:35 2022

@author: _Mumu
Environment: py38
"""

from typing import List


class Solution:
    def busyStudent(self, startTime: List[int], endTime: List[int], queryTime: int) -> int:
        ans = 0
        for start, end in zip(startTime, endTime):
            if start <= queryTime <= end:
                ans += 1
        return ans


if __name__ == '__main__':
    s = Solution()
    print(s.busyStudent(startTime=[1, 1, 1, 1], endTime=[1, 3, 2, 4], queryTime=7))
