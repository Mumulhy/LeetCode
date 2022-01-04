# -*- coding: utf-8 -*-
# LeetCode 913-猫和老鼠

"""
Created on Tues Jan 4 10:25 2022

@author: _Mumu
Environment: py38
"""

from functools import lru_cache
from typing import List


class Solution:
    def catMouseGame(self, graph: List[List[int]]) -> int:
        DRAW = 0
        MOUSE_WIN = 1
        CAT_WIN = 2
        turns = 2 * len(graph)

        @lru_cache(None)
        def search(mouse, cat, turn):
            if turn == turns:
                return DRAW
            if mouse == 0:
                return MOUSE_WIN
            if cat == mouse:
                return CAT_WIN
            curr_move = mouse if turn & 1 == 0 else cat
            default_res = CAT_WIN if curr_move == mouse else MOUSE_WIN
            res = default_res
            for next_move in graph[curr_move]:
                if next_move == 0 and curr_move == cat:
                    continue
                next_mouse = next_move if curr_move == mouse else mouse
                next_cat = next_move if curr_move == cat else cat
                next_res = search(next_mouse, next_cat, turn + 1)
                if next_res != default_res:
                    res = next_res
                    if res != DRAW:
                        break
            return res

        return search(1, 2, 0)

    # def __init__(self):
    #     self.DRAW = 0
    #     self.MOUTH_WIN = 1
    #     self.CAT_WIN = 2
    #     self.graph = []
    #     self.n = 0
    #     self.turns = 0
    #     self.dp = []
    #
    # def catMouseGame(self, graph: List[List[int]]) -> int:
    #     self.graph = graph
    #     self.n = len(graph)
    #     self.turns = 2 * self.n
    #     self.dp = [[[-1] * self.turns for _ in range(self.n)] for _ in range(self.n)]
    #     return self.getResult(1, 2, 0)
    #
    # def getResult(self, mouse: int, cat: int, turn: int) -> int:
    #     if turn == self.turns:
    #         return self.DRAW
    #     res = self.dp[mouse][cat][turn]
    #     if res != -1:
    #         return res
    #     if mouse == 0:
    #         res = self.MOUTH_WIN
    #     elif cat == mouse:
    #         res = self.CAT_WIN
    #     else:
    #         res = self.getNextResult(mouse, cat, turn)
    #     self.dp[mouse][cat][turn] = res
    #     return res
    #
    # def getNextResult(self, mouse: int, cat: int, turn: int) -> int:
    #     curr_move = mouse if turn & 1 == 0 else cat
    #     default_res = self.MOUTH_WIN if curr_move != mouse else self.CAT_WIN
    #     res = default_res
    #     for next_move in self.graph[curr_move]:
    #         if next_move == 0 and curr_move == cat:
    #             continue
    #         next_mouse = next_move if curr_move == mouse else mouse
    #         next_cat = next_move if curr_move == cat else cat
    #         next_res = self.getResult(next_mouse, next_cat, turn + 1)
    #         if next_res != default_res:
    #             res = next_res
    #             if res != self.DRAW:
    #                 break
    #     return res


if __name__ == '__main__':
    s = Solution()
    print(s.catMouseGame(graph=[[2, 5], [3], [0, 4, 5], [1, 4, 5], [2, 3], [0, 2, 3]]))
