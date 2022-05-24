# -*- coding: utf-8 -*-
# LeetCode 965-单值二叉树

"""
Created on Tues May 24 10:15 2022

@author: _Mumu
Environment: py38
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isUnivalTree(self, root: TreeNode) -> bool:
        val = root.val

        def dfs(node: TreeNode) -> bool:
            if node is None:
                return True
            return node.val == val and dfs(node.left) and dfs(node.right)

        return dfs(root)
