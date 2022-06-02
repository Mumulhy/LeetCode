# -*- coding: utf-8 -*-
# LeetCode 450-删除二叉搜索树中的节点

"""
Created on Thu Jun 2 09:32 2022

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
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if not root:
            return None

        if root.val == key:
            if not root.left:
                return root.right
            if not root.right:
                return root.left
            node = root.right
            while node.left:
                node = node.left
            root.right = self.deleteNode(root.right, node.val)
            root.val = node.val
        elif root.val < key:
            root.right = self.deleteNode(root.right, key)
        else:
            root.left = self.deleteNode(root.left, key)
        return root

        # if not root:
        #     return None
        #
        # node = root
        # father = None
        # while node and node.val != key:
        #     father = node
        #     if node.val > key:
        #         node = node.left
        #     else:
        #         node = node.right
        # if not node:
        #     return root
        #
        # to_del = node
        # if not to_del.left:
        #     if not father:
        #         return to_del.right
        #     if father.val > key:
        #         father.left = to_del.right
        #     else:
        #         father.right = to_del.right
        #     return root
        #
        # if not to_del.right:
        #     if not father:
        #         return to_del.left
        #     if father.val > key:
        #         father.left = to_del.left
        #     else:
        #         father.right = to_del.left
        #     return root
        #
        # node = to_del.left
        # mother = None
        # while node.right:
        #     mother = node
        #     node = node.right
        # to_del.val = node.val
        # if mother:
        #     mother.right = node.left
        # else:
        #     to_del.left = node.left
        # return root
