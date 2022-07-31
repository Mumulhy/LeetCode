# -*- coding: utf-8 -*-
# LeetCode 593-有效的正方形

"""
Created on Fri Jul 29 10:34 2022

@author: _Mumu
Environment: py38
"""

from typing import List


def is_par(r: List[List[int]]) -> int:
    for i in range(3):
        if r[i][0] == r[(i + 1) % 3][0] + r[(i + 2) % 3][0] and r[i][1] == r[(i + 1) % 3][1] + r[(i + 2) % 3][1]:
            return i
    return -1


def is_rec(x1: int, y1: int, x2: int, y2: int) -> bool:
    return y1 * y2 + x1 * x2 == 0


def is_sqr(x1: int, y1: int, x2: int, y2: int) -> bool:
    return x1 ** 2 + y1 ** 2 == x2 ** 2 + y2 ** 2


class Solution:
    def validSquare(self, p1: List[int], p2: List[int], p3: List[int], p4: List[int]) -> bool:
        if p1[0] == p2[0] and p1[1] == p2[1]:
            return False
        r = [[p2[0] - p1[0], p2[1] - p1[1]], [p3[0] - p1[0], p3[1] - p1[1]], [p4[0] - p1[0], p4[1] - p1[1]]]
        if (idx := is_par(r)) == -1:
            return False
        x1, y1 = r[(idx + 1) % 3]
        x2, y2 = r[(idx + 2) % 3]
        return is_rec(x1, y1, x2, y2) and is_sqr(x1, y1, x2, y2)


if __name__ == '__main__':
    s = Solution()
    print(s.validSquare(p1=[2, 3], p2=[0, 0], p3=[5, 1], p4=[3, -2]))
