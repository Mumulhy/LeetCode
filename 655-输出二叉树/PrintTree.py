# -*- coding: utf-8 -*-
# LeetCode 655-输出二叉树

"""
Created on Mon Aug 22 09:36 2022

@author: _Mumu
Environment: py39
"""

from typing import List, Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def printTree(self, root: Optional[TreeNode]) -> List[List[str]]:
        tree = []
        stack = [root]
        while stack:
            new_stack = []
            line = []
            is_node_exist = False
            for node in stack:
                if node:
                    line.append(str(node.val))
                    new_stack.append(node.left)
                    new_stack.append(node.right)
                    if node.left or node.right:
                        is_node_exist = True
                else:
                    line.append('')
                    new_stack.extend([None, None])
            stack = new_stack if is_node_exist else []
            tree.append(line)

        h = len(tree) - 1
        w = 2 ** (h + 1) - 1
        ans = [[''] * w for _ in range(h + 1)]
        ans[0][w // 2] = tree[0][0]
        tree[0][0] = w // 2
        for i in range(h):
            for j in range(2 ** (i + 1)):
                if j & 1 == 0:
                    c = tree[i][j // 2] - 2 ** (h - i - 1)
                else:
                    c = tree[i][j // 2] + 2 ** (h - i - 1)
                ans[i + 1][c] = tree[i + 1][j]
                tree[i + 1][j] = c
        return ans
