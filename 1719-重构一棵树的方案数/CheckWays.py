# -*- coding: utf-8 -*-
# LeetCode 1719-重构一棵树的方案数

"""
Created on Wed Feb 16 21:12 2022

@author: _Mumu
Environment: py38
"""

from collections import defaultdict
from typing import List


class Solution:
    def checkWays(self, pairs: List[List[int]]) -> int:
        adj = defaultdict(set)
        for x, y in pairs:
            adj[x].add(y)
            adj[y].add(x)

        n = len(adj)
        deg = {}
        root = None
        for node in adj:
            deg[node] = len(adj[node])
            if deg[node] == n - 1:
                root = node
        if not root:
            return 0

        deg[-1] = n
        ans = 1
        for node, neighbours in adj.items():
            if node == root:
                continue
            parent = -1
            for neighbour in neighbours:
                if deg[node] <= deg[neighbour] < deg[parent]:
                    parent = neighbour
            if parent == -1 or (neighbours & adj[parent]) | {parent} != neighbours:
                return 0

            if deg[parent] == deg[node]:
                ans = 2
        return ans


if __name__ == '__main__':
    s = Solution()
    print(s.checkWays([[1, 2], [2, 3], [2, 4], [1, 5]]))
