# -*- coding: utf-8 -*-
# LeetCode 429-N 叉树的层序遍历

"""
Created on Fri Apr 8 10:18 2022

@author: _Mumu
Environment: py38
"""

from typing import List


# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children


class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        if root is None:
            return []
        stack = [root]
        ans = []
        while stack:
            ans.append([])
            new_stack = []
            for node in stack:
                ans[-1].append(node.val)
                new_stack.extend(node.children)
            stack = new_stack
        return ans
