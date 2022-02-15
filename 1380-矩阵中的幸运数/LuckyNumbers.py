# -*- coding: utf-8 -*-
# LeetCode 1380-矩阵中的幸运数

"""
Created on Tues Feb 15 11:43 2022

@author: _Mumu
Environment: py38
"""

from typing import List


class Solution:
    def luckyNumbers(self, matrix: List[List[int]]) -> List[int]:
        mins = [min(line) for line in matrix]
        tar = max(mins)
        i = mins.index(tar)
        j = matrix[i].index(tar)
        for k in range(len(matrix)):
            if tar < matrix[k][j]:
                return []
        return [tar]

        # n = len(matrix)
        # ans = []
        # for line in matrix:
        #     j = line.index(min(line))
        #     is_max = True
        #     for i in range(n):
        #         if line[j] < matrix[i][j]:
        #             is_max = False
        #             break
        #     if is_max:
        #         ans.append(line[j])
        # return ans


if __name__ == '__main__':
    s = Solution()
    print(s.luckyNumbers([[7, 8], [1, 2]]))
