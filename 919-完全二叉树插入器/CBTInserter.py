# -*- coding: utf-8 -*-
# LeetCode 919-完全二叉树插入器

"""
Created on Mon Jul 25 10:27 2022

@author: _Mumu
Environment: py38
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class CBTInserter:
    def __init__(self, root: TreeNode):
        self.root = root
        self.last_layer = []
        self.curr_layer = [root]
        not_bottom = True
        while not_bottom:
            self.last_layer = self.curr_layer
            self.curr_layer = []
            for node in self.last_layer:
                if node.left:
                    self.curr_layer.append(node.left)
                if node.right:
                    self.curr_layer.append(node.right)
                else:
                    not_bottom = False
                    break
        self.last_len = len(self.last_layer)
        self.curr_len = len(self.curr_layer)

    def insert(self, val: int) -> int:
        new_node = TreeNode(val)
        ans = self.last_layer[self.curr_len // 2].val
        if self.curr_len & 1:
            self.last_layer[self.curr_len // 2].right = new_node
        else:
            self.last_layer[self.curr_len // 2].left = new_node
        self.curr_layer.append(new_node)
        self.curr_len += 1
        if self.curr_len == 2 * self.last_len:
            self.last_layer = self.curr_layer
            self.curr_layer = []
            self.last_len = self.curr_len
            self.curr_len = 0
        return ans

    def get_root(self) -> TreeNode:
        return self.root

# Your CBTInserter object will be instantiated and called as such:
# obj = CBTInserter(root)
# param_1 = obj.insert(val)
# param_2 = obj.get_root()
