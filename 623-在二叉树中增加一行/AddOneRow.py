# -*- coding: utf-8 -*-
# LeetCode 623-在二叉树中增加一行

"""
Created on Fri Aug 5 09:53 2022

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
    def addOneRow(self, root: Optional[TreeNode], val: int, depth: int) -> Optional[TreeNode]:
        if depth == 1:
            return TreeNode(val, left=root)
        stack = [root]
        while depth > 2:
            new_stack = []
            for node in stack:
                if node.left:
                    new_stack.append(node.left)
                if node.right:
                    new_stack.append(node.right)
            stack = new_stack
            depth -= 1
        for node in stack:
            node.left = TreeNode(val, left=node.left)
            node.right = TreeNode(val, right=node.right)
        return root
