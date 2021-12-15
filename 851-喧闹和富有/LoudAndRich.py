# -*- coding: utf-8 -*-
# LeetCode 851-喧闹和富有

"""
Created on Tues Dec 15 12:15 2021

@author: _Mumu
Environment: py38
"""

from typing import List


class Solution:
    def __init__(self):
        self.g = None
        self.ans = None
        self.quiet = None

    def loudAndRich(self, richer: List[List[int]], quiet: List[int]) -> List[int]:
        n = len(quiet)
        self.g = [[] for _ in range(n)]
        self.ans = [-1] * n
        self.quiet = quiet
        for pair in richer:
            self.g[pair[1]].append(pair[0])
        for i in range(n):
            self._dfs(i)
        return self.ans

    def _dfs(self, idx: int) -> None:
        if self.ans[idx] != -1:
            return
        self.ans[idx] = idx
        for rich in self.g[idx]:
            self._dfs(rich)
            if self.quiet[self.ans[rich]] < self.quiet[self.ans[idx]]:
                self.ans[idx] = self.ans[rich]
        return

        # n = len(quiet)
        # richer_than = [{i} for i in range(n)]
        # ans = list(range(n))
        # for pair in richer:
        #     richer_than[pair[0]] |= richer_than[pair[1]]
        #     for idx in richer_than[pair[0]]:
        #         if quiet[ans[pair[0]]] < quiet[ans[idx]]:
        #             ans[idx] = ans[pair[0]]
        # return ans


if __name__ == '__main__':
    s = Solution()
    print(s.loudAndRich(richer=[[1, 0], [2, 1], [3, 1], [3, 7], [4, 3], [5, 3], [6, 3]],
                        quiet=[3, 2, 5, 4, 6, 1, 7, 0]))
