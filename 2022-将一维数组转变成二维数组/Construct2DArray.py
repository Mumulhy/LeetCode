# -*- coding: utf-8 -*-
# LeetCode 2022-将一维数组转变成二维数组

"""
Created on Sat Jan 1 15:20 2022

@author: _Mumu
Environment: py38
"""

from typing import List


class Solution:
    def construct2DArray(self, original: List[int], m: int, n: int) -> List[List[int]]:
        return [original[i * n:(i + 1) * n] for i in range(m)] if len(original) == m * n else []


if __name__ == '__main__':
    s = Solution()
    print(s.construct2DArray(original=[3], m=1, n=2))
