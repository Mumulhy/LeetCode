# -*- coding: utf-8 -*-
# LeetCode 793-阶乘函数后K个零

"""
Created on Sun Aug 28 09:13 2022

@author: _Mumu
Environment: py38
"""

from bisect import bisect_left


class Solution:
    def preimageSizeFZF(self, k: int) -> int:
        divisions = [1, 6, 31, 156, 781, 3906, 19531, 97656, 488281, 2441406, 12207031, 61035156, 305175781]
        idx = bisect_left(divisions, k)
        for division, x in list(zip(divisions, range(13)))[idx:0:-1]:
            k %= division
            if k >= division - x:
                return 0
        return 5


if __name__ == '__main__':
    s = Solution()
    print(s.preimageSizeFZF(60))
