# -*- coding: utf-8 -*-
# LeetCode 998-最大二叉树II

"""
Created on Tues Aug 30 09:31 2022

@author: _Mumu
Environment: py39
"""

from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def insertIntoMaxTree(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if val > root.val:
            return TreeNode(val, root)
        node = root
        last = node
        while node.right and node.val > val:
            last = node
            node = node.right
        if node.val > val:
            node.right = TreeNode(val, node.right)
        else:
            last.right = TreeNode(val, node)
        return root
