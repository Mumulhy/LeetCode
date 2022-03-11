# -*- coding: utf-8 -*-
# LeetCode 2049-统计最高分的节点数目

"""
Created on Fri Mar 11 22:27 2022

@author: _Mumu
Environment: py38
"""

from collections import defaultdict
from typing import List


class Solution:
    def countHighestScoreNodes(self, parents: List[int]) -> int:
        n = len(parents)
        children = defaultdict(set)
        for i, j in enumerate(parents):
            if i == 0:
                continue
            children[j].add(i)

        max_score, ans = 0, 0

        def dfs(node: int) -> int:
            score = 1
            remains = n - 1
            for child in children[node]:
                size = dfs(child)
                score *= size
                remains -= size
            if node != 0:
                score *= remains
            nonlocal max_score, ans
            if score > max_score:
                max_score, ans = score, 1
            elif score == max_score:
                ans += 1
            return n - remains

        dfs(0)
        return ans

        # n = len(parents)
        # edges = defaultdict(set)
        # for i, j in enumerate(parents):
        #     if i == 0:
        #         continue
        #     edges[i].add(j)
        #     edges[j].add(i)
        # points = set(range(n))
        # max_score = -1
        # ans = 0
        # for i in range(n):
        #     not_visited = points - {i}
        #     score = 1
        #     while not_visited:
        #         j = not_visited.pop()
        #         stack = set()
        #         new_stack = edges[j] & not_visited
        #         while diff := new_stack - stack:
        #             stack = new_stack.copy()
        #             for k in diff:
        #                 new_stack |= edges[k] & not_visited
        #         score *= len(stack) + 1
        #         not_visited -= stack
        #     if score > max_score:
        #         max_score, ans = score, 1
        #     elif score == max_score:
        #         ans += 1
        # return ans


if __name__ == '__main__':
    s = Solution()
    print(s.countHighestScoreNodes([-1, 3, 3, 5, 7, 6, 0, 0]))
