# -*- coding: utf-8 -*-
# LeetCode 515-在每个树行中找最大值

"""
Created on Fri Jun 24 19:40 2022

@author: _Mumu
Environment: py38
"""

from typing import List, Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        stack = [root]
        ans = []
        while stack:
            ans.append(max(node.val for node in stack))
            new_stack = [node.left for node in stack if node.left] + [node.right for node in stack if node.right]
            stack = new_stack
        return ans
