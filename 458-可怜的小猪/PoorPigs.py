# -*- coding: utf-8 -*-
# LeetCode 458-可怜的小猪

"""
Created on Thu Nov 25 11:27 2021

@author: _Mumu
Environment: py38
"""

from math import log, ceil


class Solution:
    def poorPigs(self, buckets: int, minutesToDie: int, minutesToTest: int) -> int:
        return ceil(log(buckets) / log(minutesToTest // minutesToDie + 1))


if __name__ == '__main__':
    s = Solution()
    print(s.poorPigs(buckets=1000, minutesToDie=15, minutesToTest=60))
