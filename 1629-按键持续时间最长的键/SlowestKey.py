# -*- coding: utf-8 -*-
# LeetCode 1629-按键持续时间最长的键

"""
Created on Sun Jan 9 12:02 2022

@author: _Mumu
Environment: py38
"""

from typing import List


class Solution:
    def slowestKey(self, releaseTimes: List[int], keysPressed: str) -> str:
        n = len(releaseTimes)
        res = keysPressed[0]
        interval = releaseTimes[0]
        for i in range(1, n):
            curr_interval = releaseTimes[i] - releaseTimes[i - 1]
            if curr_interval > interval or (curr_interval == interval and keysPressed[i] > res):
                res = keysPressed[i]
                interval = curr_interval
        return res


if __name__ == '__main__':
    s = Solution()
    print(s.slowestKey(releaseTimes=[9, 29, 49, 50], keysPressed="cbcd"))
