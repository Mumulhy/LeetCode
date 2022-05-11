# -*- coding: utf-8 -*-
# LeetCode 449-序列化和反序列化二叉搜索树

"""
Created on Wed May 11 09:50 2022

@author: _Mumu
Environment: py38
"""

from collections import deque


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Codec:
    def serialize(self, root: TreeNode) -> str:
        """Encodes a tree to a single string.
        """
        return ' '.join([str(root.val), self.serialize(root.left), self.serialize(root.right)]) if root else '*'

        # if not root:
        #     return ''
        # layer = [root]
        # data = []
        # while any(layer):
        #     data_layer = []
        #     new_layer = []
        #     for node in layer:
        #         if node:
        #             data_layer.append(str(node.val))
        #             new_layer.append(node.left)
        #             new_layer.append(node.right)
        #         else:
        #             data_layer.append('*')
        #     data.append(' '.join(data_layer))
        #     layer = new_layer
        # return '|'.join(data)

    def deserialize(self, data: str) -> TreeNode:
        """Decodes your encoded data to tree.
        """
        dq = deque(data.split(' '))

        def run():
            curr = dq.popleft()
            if curr == '*':
                return None
            root = TreeNode(int(curr))
            root.left = run()
            root.right = run()
            return root

        return run()

        # if not data:
        #     return None
        # layer = []
        # root = None
        # for data_layer in data.split('|'):
        #     new_layer = []
        #     if not layer:
        #         root = TreeNode(int(data_layer))
        #         layer.append(root)
        #         continue
        #     for i, data_node in enumerate(data_layer.split(' ')):
        #         if data_node == '*':
        #             continue
        #         node = TreeNode(int(data_node))
        #         new_layer.append(node)
        #         if i & 1 == 0:
        #             layer[i >> 1].left = node
        #         else:
        #             layer[i >> 1].right = node
        #     layer = new_layer
        # return root


# Your Codec object will be instantiated and called as such:
# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# tree = ser.serialize(root)
# ans = deser.deserialize(tree)
# return ans

if __name__ == '__main__':
    c = Codec()
    root = None
    data = c.serialize(root)
    print(data)
    tree = c.deserialize(data)
    layer = [tree]
    while any(layer):
        new_layer = []
        for node in layer:
            if node:
                print(node.val, end=' ')
                new_layer.append(node.left)
                new_layer.append(node.right)
            else:
                print('*', end=' ')
                new_layer.append(None)
                new_layer.append(None)
        print()
        layer = new_layer
