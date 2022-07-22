# -*- coding: utf-8 -*-
# LeetCode 814-二叉树剪枝

"""
Created on Thu Jul 21 10:06 2022

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
    def pruneTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def process(node: TreeNode, father: Optional[TreeNode], is_left: bool) -> Optional[TreeNode]:
            if node.left:
                process(node.left, node, True)
            if node.right:
                process(node.right, node, False)
            if not node.left and not node.right and node.val == 0:
                if father:
                    if is_left:
                        father.left = None
                    else:
                        father.right = None
                else:
                    return None
            return node

        return process(root, None, True)
