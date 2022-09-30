# -*- coding: utf-8 -*-
# LeetCode 面试题01.08-零矩阵

"""
Created on Fri Sept 30 11:09 2022

@author: _Mumu
Environment: py39
"""

from typing import List


class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        m, n = len(matrix), len(matrix[0])
        keep = [[True] * n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    for ki in range(m):
                        keep[ki][j] = False
                    for kj in range(n):
                        keep[i][kj] = False
        for i in range(m):
            for j in range(n):
                matrix[i][j] *= keep[i][j]
        return
