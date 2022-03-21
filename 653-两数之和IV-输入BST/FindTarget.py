# -*- coding: utf-8 -*-
# LeetCode 653-两数之和IV-输入BST

"""
Created on Mon Mar 21 14:20 2022

@author: _Mumu
Environment: py38
"""

from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        if not root:
            return False
        stack, visited = [root], set()
        while stack:
            new_stack = []
            for node in stack:
                if k - node.val in visited:
                    return True
                visited.add(node.val)
                if node.left:
                    new_stack.append(node.left)
                if node.right:
                    new_stack.append(node.right)
            stack = new_stack
        return False
