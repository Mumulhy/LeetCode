# -*- coding: utf-8 -*-
# LeetCode 1893-检查是否区域内所有整数都被覆盖

"""
Created on Fri Jul 23 21:09 2021

@author: _Mumu
Environment: py38
"""

from typing import List


class Solution:
    def isCovered(self, ranges: List[List[int]], left: int, right: int) -> bool:
        covered = 0
        for _range in ranges:
            covered |= (1 << _range[1]) - (1 << _range[0] - 1)
        tar = (1 << right) - (1 << left - 1)
        if covered & tar == tar:
            return True
        else:
            return False


if __name__ == '__main__':
    s = Solution()
    print(s.isCovered(ranges=[[1, 10], [10, 20]], left=17, right=21))
