# -*- coding: utf-8 -*-
# LeetCode 495-提莫攻击

"""
Created on Wed Nov 10 12:24 2021

@author: _Mumu
Environment: py38
"""

from typing import List


class Solution:
    def findPoisonedDuration(self, timeSeries: List[int], duration: int) -> int:
        poisoned = 0
        for i in range(len(timeSeries) - 1):
            if timeSeries[i + 1] >= timeSeries[i] + duration:
                poisoned += duration
            else:
                poisoned += timeSeries[i + 1] - timeSeries[i]
        poisoned += duration
        return poisoned


if __name__ == '__main__':
    s = Solution()
    print(s.findPoisonedDuration(timeSeries=[1], duration=2))
