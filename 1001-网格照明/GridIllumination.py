# -*- coding: utf-8 -*-
# LeetCode 1001-网格照明

"""
Created on Tues Feb 8 15:25 2022

@author: _Mumu
Environment: py38
"""

from collections import defaultdict
from typing import List


class Solution:
    def gridIllumination(self, n: int, lamps: List[List[int]], queries: List[List[int]]) -> List[int]:
        alight = set()
        rows, cols, diag1, diag2 = defaultdict(int), defaultdict(int), defaultdict(int), defaultdict(int)
        for lamp_r, lamp_c in lamps:
            if (lamp_r, lamp_c) in alight:
                continue
            alight.add((lamp_r, lamp_c))
            rows[lamp_r] += 1
            cols[lamp_c] += 1
            diag1[lamp_r - lamp_c] += 1
            diag2[lamp_r + lamp_c] += 1
        ans = []
        for query_r, query_c in queries:
            if query_r in rows or query_c in cols or query_r - query_c in diag1 or query_r + query_c in diag2:
                ans.append(1)
            else:
                ans.append(0)
            for neighbour_r in range(query_r - 1, query_r + 2):
                for neighbour_c in range(query_c - 1, query_c + 2):
                    if (neighbour_r, neighbour_c) in alight:
                        alight.remove((neighbour_r, neighbour_c))
                        rows[neighbour_r] -= 1
                        cols[neighbour_c] -= 1
                        diag1[neighbour_r - neighbour_c] -= 1
                        diag2[neighbour_r + neighbour_c] -= 1
                        if rows[neighbour_r] == 0:
                            rows.pop(neighbour_r)
                        if cols[neighbour_c] == 0:
                            cols.pop(neighbour_c)
                        if diag1[neighbour_r - neighbour_c] == 0:
                            diag1.pop(neighbour_r - neighbour_c)
                        if diag2[neighbour_r + neighbour_c] == 0:
                            diag2.pop(neighbour_r + neighbour_c)
        return ans


if __name__ == '__main__':
    s = Solution()
    print(s.gridIllumination(n=5, lamps=[[0, 0], [0, 4]], queries=[[0, 4], [0, 1], [1, 4]]))
