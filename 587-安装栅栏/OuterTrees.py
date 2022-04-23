# -*- coding: utf-8 -*-
# LeetCode 587-安装栅栏

"""
Created on Sat Apr 23 12:03 2022

@author: _Mumu
Environment: py38
"""

from typing import List


class Solution:
    def outerTrees(self, trees: List[List[int]]) -> List[List[int]]:
        def cross(p: List[int], q: List[int], r: List[int]) -> bool:
            return (q[1] - p[1]) * (r[0] - q[0]) - (r[1] - q[1]) * (q[0] - p[0]) > 0

        n = len(trees)
        if n < 4:
            return trees

        trees.sort()
        outer = [0]
        used = [False] * n
        for i in range(1, n):
            while len(outer) > 1 and cross(trees[outer[-2]], trees[outer[-1]], trees[i]):
                used[outer.pop()] = False
            used[i] = True
            outer.append(i)
        m = len(outer)
        for i in range(n - 2, -1, -1):
            if not used[i]:
                while len(outer) > m and cross(trees[outer[-2]], trees[outer[-1]], trees[i]):
                    used[outer.pop()] = False
                used[i] = True
                outer.append(i)
        return [trees[i] for i in outer[:-1]]


if __name__ == '__main__':
    s = Solution()
    print(s.outerTrees([[1, 1], [2, 2], [2, 0], [2, 4], [3, 3], [4, 2]]))
