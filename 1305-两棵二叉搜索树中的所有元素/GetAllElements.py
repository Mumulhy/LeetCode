# -*- coding: utf-8 -*-
# LeetCode 1305-两棵二叉搜索树中的所有元素

"""
Created on Sun May 1 09:25 2022

@author: _Mumu
Environment: py38
"""

from typing import List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def getAllElements(self, root1: TreeNode, root2: TreeNode) -> List[int]:
        tree = []

        def get_tree(node: TreeNode) -> None:
            if node.left:
                get_tree(node.left)
            tree.append(node.val)
            if node.right:
                get_tree(node.right)
            return

        if root1:
            get_tree(root1)
        tree1 = tree.copy()
        tree.clear()
        if root2:
            get_tree(root2)
        ans = []
        m, n, i, j = len(tree1), len(tree), 0, 0
        while i < m and j < n:
            while i < m and tree1[i] <= tree[j]:
                ans.append(tree1[i])
                i += 1
            while i < m and j < n and tree[j] <= tree1[i]:
                ans.append(tree[j])
                j += 1
        if i < m:
            while i < m:
                ans.append(tree1[i])
                i += 1
        elif j < n:
            while j < n:
                ans.append(tree[j])
                j += 1
        return ans
