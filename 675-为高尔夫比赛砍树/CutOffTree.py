# -*- coding: utf-8 -*-
# LeetCode 675-为高尔夫比赛砍树

"""
Created on Mon May 23 10:47 2022

@author: _Mumu
Environment: py38
"""

from heapq import heappush, heappop
from typing import List


class Solution:
    def __init__(self):
        self.map = []
        self.m = 0
        self.n = 0

    def cutOffTree(self, forest: List[List[int]]) -> int:
        self.map = forest
        self.m = len(forest)
        self.n = len(forest[0])
        left2cut = []
        for x in range(self.m):
            for y in range(self.n):
                if self.map[x][y] > 1:
                    heappush(left2cut, self.map[x][y])
        ans = 0
        start = [0, 0]
        while left2cut:
            target = heappop(left2cut)
            start, step = self.find_way(start, target)
            if step == -1:
                return -1
            ans += step
        return ans

    def find_way(self, start: List[int], target: int) -> List[List[int]]:
        stack = {tuple(start)}
        visited = stack.copy()
        diff = [-1, 0, 1, 0, -1]
        step = 0
        while stack:
            for x, y in stack:
                if self.map[x][y] == target:
                    return [[x, y], step]
            new_stack = set()
            for x, y in stack:
                for i in range(4):
                    neighbour_x, neighbour_y = x + diff[i], y + diff[i + 1]
                    if (0 <= neighbour_x < self.m and 0 <= neighbour_y < self.n
                            and (neighbour_x, neighbour_y) not in visited
                            and self.map[neighbour_x][neighbour_y] != 0):
                        new_stack.add((neighbour_x, neighbour_y))
            stack = new_stack
            visited |= stack
            step += 1
        return [[0, 0], -1]


if __name__ == '__main__':
    s = Solution()
    print(s.cutOffTree([[4, 3, 2], [0, 0, 5], [8, 7, 6]]))
