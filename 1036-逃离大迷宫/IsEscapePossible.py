# -*- coding: utf-8 -*-
# LeetCode 1036-逃离大迷宫

"""
Created on Tues Jan 11 10:28 2022

@author: _Mumu
Environment: py38
"""

# from heapq import heappop, heappush
from typing import List


class Solution:
    def __init__(self):
        self.blocked = set()
        self.target = []
        self.start = []
        self.closed_from_start = set()
        self.closed_from_target = set()
        self.BOUND = 999999
        self.MAX_LOOP = 0

    def isEscapePossible(self, blocked: List[List[int]], source: List[int], target: List[int]) -> bool:
        if len(blocked) < 2:
            return True
        self.blocked = {tuple(point) for point in blocked}
        self.target = target
        self.start = source
        n = len(blocked)
        self.MAX_LOOP = (n - 1) * n // 2 + 1
        node_to_process = {(source[0], source[1])}
        nodes_from_start = 1
        shut_down = False
        while node_to_process:
            curr_node_x, curr_node_y = node_to_process.pop()
            neighbours = self.getNeighbours(curr_node_x, curr_node_y, self.isClosedFromStart)
            for neighbour_x, neighbour_y in neighbours:
                if self.isTarget(neighbour_x, neighbour_y):
                    return True
                nodes_from_start += 1
                if nodes_from_start > self.MAX_LOOP:
                    shut_down = True
                    break
                node_to_process.add((neighbour_x, neighbour_y))
                self.closeThePointFromStart(neighbour_x, neighbour_y)
        if shut_down is False:
            return False
        node_to_process = {(target[0], target[1])}
        nodes_from_target = 1
        while node_to_process:
            curr_node_x, curr_node_y = node_to_process.pop()
            neighbours = self.getNeighbours(curr_node_x, curr_node_y, self.isClosedFromTarget)
            for neighbour_x, neighbour_y in neighbours:
                if self.isStart(neighbour_x, neighbour_y) or self.isClosedFromStart(neighbour_x, neighbour_y):
                    return True
                nodes_from_target += 1
                if nodes_from_target >= self.MAX_LOOP:
                    return True
                node_to_process.add((neighbour_x, neighbour_y))
                self.closeThePointFromTarget(neighbour_x, neighbour_y)
        return False

    def isTarget(self, x: int, y: int) -> bool:
        return x == self.target[0] and y == self.target[1]

    def isStart(self, x: int, y: int) -> bool:
        return x == self.start[0] and y == self.start[1]

    def isClosedFromStart(self, x: int, y: int) -> bool:
        return (x, y) in self.closed_from_start

    def isClosedFromTarget(self, x: int, y: int) -> bool:
        return (x, y) in self.closed_from_target

    def isOutBound(self, x: int, y: int) -> bool:
        return x < 0 or y < 0 or x > self.BOUND or y > self.BOUND

    def isBlocked(self, x: int, y: int) -> bool:
        return (x, y) in self.blocked

    def closeThePointFromStart(self, x: int, y: int) -> None:
        self.closed_from_start.add((x, y))
        return

    def closeThePointFromTarget(self, x: int, y: int) -> None:
        self.closed_from_target.add((x, y))
        return

    def getNeighbours(self, x: int, y: int, isClosed) -> List[List[int]]:
        diff = [-1, 0, 1, 0, -1]
        loop = 4
        neighbours = []
        for i in range(loop):
            neighbour_x = x + diff[i]
            neighbour_y = y + diff[i + 1]
            if (isClosed(neighbour_x, neighbour_y)
                    or self.isOutBound(neighbour_x, neighbour_y)
                    or self.isBlocked(neighbour_x, neighbour_y)):
                continue
            neighbours.append([neighbour_x, neighbour_y])
        return neighbours


if __name__ == '__main__':
    s = Solution()
    print(s.isEscapePossible(blocked=[], source=[0, 0], target=[999999, 999999]))
