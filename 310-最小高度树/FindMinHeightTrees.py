# -*- coding: utf-8 -*-
# LeetCode 310-最小高度树

"""
Created on Wed Apr 6 09:39 2022

@author: _Mumu
Environment: py38
"""

from collections import defaultdict
from typing import List


class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        graph = defaultdict(set)
        for x, y in edges:
            graph[x].add(y)
            graph[y].add(x)
        dest = 0
        ans = []
        for _ in range(2):
            root = dest
            stack = {root}
            dist = 0
            vis = {root}
            father = {}
            while stack:
                new_stack = set()
                for node in stack:
                    new_stack |= graph[node] - vis
                    for child in graph[node] - vis:
                        father[child] = node
                if not new_stack:
                    break
                stack = new_stack.copy()
                dist += 1
                vis |= new_stack
            dest = next(iter(stack))
        mid = dest
        for _ in range(dist // 2):
            mid = father[mid]
        ans.append(mid)
        if dist & 1 == 1:
            ans.append(father[mid])
        return ans


if __name__ == '__main__':
    s = Solution()
    print(s.findMinHeightTrees(n=6, edges=[[3, 0], [3, 1], [3, 2], [3, 4], [5, 4]]))
