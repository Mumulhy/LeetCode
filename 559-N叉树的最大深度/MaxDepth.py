# -*- coding: utf-8 -*-
# LeetCode 559-N叉树的最大深度

"""
Created on Sun Nov 21 09:57 2021

@author: _Mumu
Environment: py38
"""


# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children


class Solution:
    def __init__(self):
        self.depth = 1

    def maxDepth(self, root: 'Node') -> int:
        if not root:
            return 0
        self._findDepth(root, 1)
        return self.depth

    def _findDepth(self, node: 'Node', curr_depth: int) -> None:
        curr_depth += 1
        if node.children:
            self.depth = max(self.depth, curr_depth)
        for child in node.children:
            self._findDepth(child, curr_depth)

    # def maxDepth(self, root: 'Node') -> int:
    #     return max((self.maxDepth(child) for child in root.children), default=0) + 1 if root else 0
