# -*- coding: utf-8 -*-
# LeetCode 2039-网络空闲的时刻

"""
Created on Sun Mar 20 13:52 2022

@author: _Mumu
Environment: py38
"""

from collections import defaultdict
from typing import List


class Solution:
    def networkBecomesIdle(self, edges: List[List[int]], patience: List[int]) -> int:
        graph = defaultdict(set)
        for x, y in edges:
            graph[x].add(y)
            graph[y].add(x)
        stack, new_stack = graph[0], set()
        visited = {0}
        step, ans = 1, 0
        while stack:
            visited |= stack
            for x in stack:
                ans = max(ans, 2 * step + ((2 * step - 1) // patience[x]) * patience[x])
                new_stack |= graph[x]
            new_stack -= visited
            stack = new_stack.copy()
            step += 1
        return ans + 1


if __name__ == '__main__':
    s = Solution()
    print(s.networkBecomesIdle(edges=[[0, 1], [1, 2]], patience=[0, 2, 1]))
