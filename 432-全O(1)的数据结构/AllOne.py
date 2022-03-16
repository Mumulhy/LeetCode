# -*- coding: utf-8 -*-
# LeetCode 432-全O(1)的数据结构

"""
Created on Wed Mar 16 10:38 2022

@author: _Mumu
Environment: py38
"""


class Node:
    def __init__(self, key: str, cnt: int = 0):
        self.prev = None
        self.next = None
        self.keys = {key}
        self.cnt = cnt

    def insert(self, node: 'Node') -> 'Node':
        node.prev = self
        node.next = self.next
        self.next = node
        node.next.prev = node
        return node

    def remove(self):
        self.prev.next = self.next
        self.next.prev = self.prev
        del self
        return


class AllOne:
    def __init__(self):
        self.root = Node('')
        self.root.prev = self.root
        self.root.next = self.root
        self.nodes = {}

    def inc(self, key: str) -> None:
        if key in self.nodes:
            cur = self.nodes[key]
            nxt = cur.next
            if nxt is self.root or nxt.cnt > cur.cnt + 1:
                self.nodes[key] = cur.insert(Node(key, cur.cnt + 1))
            else:
                nxt.keys.add(key)
                self.nodes[key] = nxt
            cur.keys.remove(key)
            if not cur.keys:
                cur.remove()
        else:
            if self.root.next is self.root or self.root.next.cnt > 1:
                self.nodes[key] = self.root.insert(Node(key, 1))
            else:
                self.root.next.keys.add(key)
                self.nodes[key] = self.root.next
        return

    def dec(self, key: str) -> None:
        cur = self.nodes[key]
        if cur.cnt == 1:
            self.nodes.pop(key)
        else:
            pre = cur.prev
            if pre is self.root or pre.cnt < cur.cnt - 1:
                self.nodes[key] = pre.insert(Node(key, cur.cnt - 1))
            else:
                pre.keys.add(key)
                self.nodes[key] = pre
        cur.keys.remove(key)
        if not cur.keys:
            cur.remove()
        return

    def getMaxKey(self) -> str:
        return next(iter(self.root.prev.keys)) if self.root.prev is not self.root else ''

    def getMinKey(self) -> str:
        return next(iter(self.root.next.keys)) if self.root.next is not self.root else ''

# Your AllOne object will be instantiated and called as such:
# obj = AllOne()
# obj.inc(key)
# obj.dec(key)
# param_3 = obj.getMaxKey()
# param_4 = obj.getMinKey()
