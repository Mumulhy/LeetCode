# -*- coding: utf-8 -*-
# LeetCode 1582-二进制矩阵中的特殊位置

"""
Created on Sun Sept 4 11:01 2022

@author: _Mumu
Environment: py38
"""

from typing import List


class Solution:
    def numSpecial(self, mat: List[List[int]]) -> int:
        m, n = len(mat), len(mat[0])
        raws = [sum(raw) for raw in mat]
        cols = [sum(raw[j] for raw in mat) for j in range(n)]
        ans = 0
        for i in range(m):
            for j in range(n):
                if raws[i] == cols[j] == mat[i][j] == 1:
                    ans += 1
        return ans


if __name__ == '__main__':
    s = Solution()
    print(s.numSpecial([[1, 0, 0],
                        [0, 0, 1],
                        [1, 0, 0]]))
