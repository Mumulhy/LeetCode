# -*- coding: utf-8 -*-
# LeetCode 542-01矩阵

"""
Created on Wed Feb 17 15:03 2021

@author: _Mumu
Environment: py37
"""

class Solution:
    def updateMatrix(self, matrix):
        res_matrix = [[0 for item in row] for row in matrix]
        while sum(sum(matrix, [])):
            res_matrix = self.plusMatrix(res_matrix, matrix)
            matrix = self.nextLayer(matrix)
        return res_matrix

    def nextLayer(self, matrix):
        m = len(matrix)
        n = len(matrix[0])
        ori_matrix = [[item for item in row] for row in matrix]
        for i in range(m):
            for j in range(n):
                if matrix[i][j]:
                    is_not_edge = 1
                    if i != 0:
                        is_not_edge = is_not_edge * ori_matrix[i-1][j]
                    if i != m-1:
                        is_not_edge = is_not_edge * ori_matrix[i+1][j]
                    if j != 0:
                        is_not_edge = is_not_edge * ori_matrix[i][j-1]
                    if j != n-1:
                        is_not_edge = is_not_edge * ori_matrix[i][j+1]
                    if is_not_edge == 0:
                        matrix[i][j] = 0
        return matrix

    def plusMatrix(self, matrixA, matrixB):
        m = len(matrixA)
        n = len(matrixA[0])
        return [[matrixA[i][j]+matrixB[i][j] for j in range(n)] for i in range(m)]

# 以下是运行速度最快的代码

# class Solution:
#     def updateMatrix(self, matrix: List[List[int]]) -> List[List[int]]:
#         row = len(matrix)
#         col = len(matrix[0])
#         for i in range(row):
#             for j in range(col):
#                 if matrix[i][j]:
#                     up = matrix[i - 1][j] if i else float('inf')
#                     left = matrix[i][j - 1] if j else float('inf')
#                     matrix[i][j] = min(up, left) + 1
#         for i in range(row - 1, -1, -1):
#             for j in range(col - 1, -1, -1):
#                 if matrix[i][j]:
#                     down = matrix[i + 1][j] if i < row - 1 else float('inf')
#                     right = matrix[i][j + 1] if j < col - 1 else float('inf')
#                     matrix[i][j] = min(matrix[i][j], down + 1, right + 1)
#         return matrix

if __name__ == '__main__':
    s = Solution()
    matrix = [[0, 0, 0],
              [0, 1, 0],
              [1, 1, 1]]
    print(s.updateMatrix(matrix))