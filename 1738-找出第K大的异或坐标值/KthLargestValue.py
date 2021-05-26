# -*- coding: utf-8 -*-
# LeetCode 1738-找出第K大的异或坐标值

"""
Created on Fri May 19 21:59 2021

@author: _Mumu
Environment: py38
"""


class Solution:
    def kthLargestValue(self, matrix: list, k: int) -> int:
        m = len(matrix)
        n = len(matrix[0])
        xor_matrix = [[0] * (n + 1) for _ in range(m + 1)]
        xor_list = []
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                xor_matrix[i][j] = matrix[i - 1][j - 1] ^ xor_matrix[i - 1][j] ^ xor_matrix[i][j - 1] ^ \
                                   xor_matrix[i - 1][j - 1]
                xor_list.append(xor_matrix[i][j])
        xor_list.sort()
        return xor_list[-k]


if __name__ == '__main__':
    s = Solution()
    print(s.kthLargestValue([[10, 9, 5], [2, 0, 4], [1, 0, 9], [3, 4, 8]], 10))
