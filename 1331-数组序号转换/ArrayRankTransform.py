# -*- coding: utf-8 -*-
# LeetCode 1331-数组序号转换

"""
Created on Thu Jul 28 10:09 2022

@author: _Mumu
Environment: py38
"""

from typing import List


class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        l = sorted(set(arr))
        d = dict(zip(l, range(1, len(l) + 1)))
        return [d[num] for num in arr]


if __name__ == '__main__':
    s = Solution()
    print(s.arrayRankTransform([37, 12, 28, 9, 100, 56, 80, 5, 12]))
