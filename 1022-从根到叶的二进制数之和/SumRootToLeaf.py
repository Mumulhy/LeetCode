# -*- coding: utf-8 -*-
# LeetCode 1022-从根到叶的二进制数之和

"""
Created on Mon May 30 10:22 2022

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
    def sumRootToLeaf(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        ans = 0

        def dfs(node: TreeNode, pre: int) -> None:
            nonlocal ans
            if not node.left and not node.right:
                ans += (pre << 1) + node.val
                return
            pre = (pre << 1) + node.val
            if node.left:
                dfs(node.left, pre)
            if node.right:
                dfs(node.right, pre)
            return

        dfs(root, 0)
        return ans
