# -*- coding: utf-8 -*-
# LeetCode 427-建立四叉树

"""
Created on Fri Apr 29 10:44 2022

@author: _Mumu
Environment: py38
"""

from typing import List


# Definition for a QuadTree node.
class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight


class Solution:
    def construct(self, grid: List[List[int]]) -> 'Node':
        n = len(grid)
        is_leaf = True
        val = grid[0][0]
        for i in range(n):
            for j in range(n):
                if grid[i][j] != val:
                    is_leaf = False
                    break
            if is_leaf is False:
                break
        if is_leaf:
            return Node(val, 1, None, None, None, None)
        n >>= 1
        top_left = self.construct([row[:n] for row in grid[:n]])
        top_right = self.construct([row[n:] for row in grid[:n]])
        bottom_left = self.construct([row[:n] for row in grid[n:]])
        bottom_right = self.construct([row[n:] for row in grid[n:]])
        return Node(0, 0, top_left, top_right, bottom_left, bottom_right)
