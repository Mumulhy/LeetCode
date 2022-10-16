# -*- coding: utf-8 -*-
# LeetCode 886-可能的二分法

"""
Created on Sun Oct 16 09:50 2022

@author: _Mumu
Environment: py38
"""

from collections import defaultdict
from typing import List


class Solution:
    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:
        graph = defaultdict(set)
        for x, y in dislikes:
            graph[x].add(y)
            graph[y].add(x)
        set1 = set(range(1, n + 1))
        set2 = set(range(1, n + 1))
        stack = {1}
        vis = set()
        while len(vis) < n:
            if stack:
                node = stack.pop()
            else:
                node = (set(range(1, n + 1)) - vis).pop()
            vis.add(node)
            if node in set1:
                set1 -= graph[node]
            elif node in set2:
                set2 -= graph[node]
            else:
                return False
            stack |= graph[node] - vis
        return True


if __name__ == '__main__':
    s = Solution()
    print(s.possibleBipartition(n=5, dislikes=[[1, 2], [3, 4], [4, 5], [3, 5]]))
