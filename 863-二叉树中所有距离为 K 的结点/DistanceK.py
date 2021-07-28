# -*- coding: utf-8 -*-
# LeetCode 863-二叉树中所有距离为 K 的结点

"""
Created on Wed Jul 28 20:30 2021

@author: _Mumu
Environment: py38
"""

from collections import defaultdict
from typing import List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        if k == 0:
            return [target.val]
        graph = defaultdict(list)

        def drawGraph(node: TreeNode) -> None:
            nonlocal graph
            if node.left:
                graph[node.val].append(node.left.val)
                graph[node.left.val].append(node.val)
                drawGraph(node.left)
            if node.right:
                graph[node.val].append(node.right.val)
                graph[node.right.val].append(node.val)
                drawGraph(node.right)
            return

        drawGraph(root)
        distance_Ks = []

        def findDistanceK(node: int, distance: int, last_node: int) -> None:
            nonlocal distance_Ks
            distance += 1
            if distance == k:
                for next_node in graph[node]:
                    if next_node != last_node:
                        distance_Ks.append(next_node)
            else:
                for next_node in graph[node]:
                    if next_node != last_node:
                        findDistanceK(next_node, distance, node)
            return

        findDistanceK(target.val, 0, -1)
        return distance_Ks


if __name__ == '__main__':
    s = Solution()
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.right.left = TreeNode(4)
    root.right.right = TreeNode(5)
    root.right.left.left = TreeNode(6)
    root.right.left.right = TreeNode(7)
    root.right.right.left = TreeNode(8)
    root.right.right.right = TreeNode(9)
    root.right.right.right.left = TreeNode(10)
    root.right.right.right.right = TreeNode(11)
    print(s.distanceK(root, root.right.right, 2))
