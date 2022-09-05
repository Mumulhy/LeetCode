# -*- coding: utf-8 -*-
# LeetCode 652-寻找重复的子树

"""
Created on Mon Sept 5 10:00 2022

@author: _Mumu
Environment: py39
"""

from typing import Optional, List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def findDuplicateSubtrees(self, root: Optional[TreeNode]) -> List[Optional[TreeNode]]:
        idx = 0
        seen = {}
        repeat = set()

        def dfs(node: Optional[TreeNode]) -> int:
            if not node:
                return 0

            tri = (node.val, dfs(node.left), dfs(node.right))
            if tri in seen:
                tree, index = seen[tri]
                repeat.add(tree)
                return index
            nonlocal idx
            idx += 1
            seen[tri] = (node, idx)
            return idx

        dfs(root)
        return list(repeat)
