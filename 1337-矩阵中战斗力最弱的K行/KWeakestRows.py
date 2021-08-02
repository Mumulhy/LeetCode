# -*- coding: utf-8 -*-
# LeetCode 1337-矩阵中战斗力最弱的K行

"""
Created on Sun Aug 1 20:19 2021

@author: _Mumu
Environment: py38
"""

from typing import List


class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        from bisect import bisect_left
        n = len(mat[0])
        strengths = [(n - bisect_left(solders[::-1], 1)) * 1000 + i for i, solders in enumerate(mat)]
        return [strength % 1000 for strength in sorted(strengths)][:k]


if __name__ == '__main__':
    s = Solution()
    print(s.kWeakestRows(mat=[[1, 1, 0, 0, 0],
                              [1, 1, 1, 1, 0],
                              [1, 0, 0, 0, 0],
                              [1, 1, 0, 0, 0],
                              [1, 1, 1, 1, 1]],
                         k=3))
