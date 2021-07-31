# -*- coding: utf-8 -*-
# LeetCode 987-二叉树的垂序遍历

"""
Created on Sat Jul 31 18:25 2021

@author: _Mumu
Environment: py38
"""

from collections import defaultdict
from typing import List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def verticalTraversal(self, root: TreeNode) -> List[List[int]]:
        tree = defaultdict(list)

        def climbTree(node: TreeNode, row: int, col: int) -> None:
            nonlocal tree
            tree[col].append((row, node.val))
            if node.left:
                climbTree(node.left, row + 1, col - 1)
            if node.right:
                climbTree(node.right, row + 1, col + 1)
            return

        climbTree(root, 0, 0)
        tree_list = []
        for col in sorted(tree.keys()):
            tree_list.append([])
            for row, val in sorted(tree[col]):
                tree_list[-1].append(val)
        return tree_list


if __name__ == '__main__':
    s = Solution()
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    root.right.left = TreeNode(6)
    root.right.right = TreeNode(7)
    print(s.verticalTraversal(root))
