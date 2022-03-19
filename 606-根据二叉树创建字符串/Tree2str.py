# -*- coding: utf-8 -*-
# LeetCode 606-根据二叉树创建字符串

"""
Created on Sat Mar 19 09:58 2022

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
    def tree2str(self, root: Optional[TreeNode]) -> str:
        if root is None:
            return ''
        if root.left is None and root.right is None:
            return str(root.val)
        if root.right is None:
            return f'{root.val}({self.tree2str(root.left)})'
        return f'{root.val}({self.tree2str(root.left)})({self.tree2str(root.right)})'

        # ans = []
        #
        # def dfs(node: Optional[TreeNode]) -> None:
        #     if not node:
        #         return
        #     ans.append(str(node.val))
        #     if node.left or node.right:
        #         ans.append('(')
        #         if node.left:
        #             dfs(node.left)
        #         ans.append(')')
        #         if node.right:
        #             ans.append('(')
        #             dfs(node.right)
        #             ans.append(')')
        #     return
        #
        # dfs(root)
        # return ''.join(ans)
