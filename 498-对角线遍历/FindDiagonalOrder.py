# -*- coding: utf-8 -*-
# LeetCode 498-对角线遍历

"""
Created on Tues Jun 14 16:35 2022

@author: _Mumu
Environment: py38
"""

from typing import List


class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        switch = False
        x, y = 0, 0
        m, n = len(mat), len(mat[0])
        ans = []
        while x < m and y < n:
            ans.append(mat[x][y])
            if switch:
                if y != 0 and x != m - 1:
                    x += 1
                    y -= 1
                    continue
                if x == m - 1:
                    y += 1
                else:
                    x += 1
                switch = False
            else:
                if x != 0 and y != n - 1:
                    x -= 1
                    y += 1
                    continue
                if y == n - 1:
                    x += 1
                else:
                    y += 1
                switch = True
        return ans


if __name__ == '__main__':
    s = Solution()
    print(s.findDiagonalOrder([[1, 2, 3, 4]]))
