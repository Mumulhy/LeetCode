# -*- coding: utf-8 -*-
# LeetCode 240-搜索二维矩阵II

"""
Created on Fri Oct 25 19:09 2021

@author: _Mumu
Environment: py38
"""

# from bisect import bisect_left
from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        x, y = 0, len(matrix[0]) - 1
        m = len(matrix)
        while x <= m - 1 and y >= 0:
            if matrix[x][y] == target:
                return True
            if matrix[x][y] < target:
                x += 1
            else:
                y -= 1
        return False

        # for row in matrix:
        #     if target < row[0]:
        #         return False
        #     if target > row[-1]:
        #         continue
        #     if row[bisect_left(row, target)] == target:
        #         return True
        # return False


if __name__ == '__main__':
    s = Solution()
    print(s.searchMatrix(matrix=[[1, 2, 3, 4, 5],
                                 [6, 7, 8, 9, 10],
                                 [11, 12, 13, 14, 15],
                                 [16, 17, 18, 19, 20],
                                 [21, 22, 23, 24, 25]],
                         target=15))
