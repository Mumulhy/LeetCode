# -*- coding: utf-8 -*-
# LeetCode 687-最长同值路径

"""
Created on Fri Sept 2 10:48 2022

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
    def longestUnivaluePath(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        ans = 0

        def dfs(node: TreeNode) -> int:
            nonlocal ans
            if node.left:
                l = dfs(node.left)
                if node.left.val == node.val:
                    l += 1
                else:
                    l = 0
            else:
                l = 0
            if node.right:
                r = dfs(node.right)
                if node.right.val == node.val:
                    r += 1
                else:
                    r = 0
            else:
                r = 0
            ans = max(ans, l + r)
            return max(l, r)

        dfs(root)
        return ans
