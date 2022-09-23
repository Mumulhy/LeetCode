# -*- coding: utf-8 -*-
# LeetCode 707-设计链表

"""
Created on Wed Oct 2 00:07 2019
Edited on Fri Sept 23 12:45 2022

@author: _Mumu
Environment: py38
"""


class LinkedListNode:
    def __init__(self, val, nxt=None, prv=None):
        self.val = val
        self.nxt = nxt
        self.prv = prv


class MyLinkedList:
    def __init__(self):
        self.len = 0
        self.head = None
        self.tail = None

    def get(self, index: int) -> int:
        if index < 0 or index >= self.len:
            return -1
        return self.getNode(index).val

    def addAtHead(self, val: int) -> None:
        if self.len == 0:
            self.head = self.tail = LinkedListNode(val)
        else:
            new_head = LinkedListNode(val, nxt=self.head)
            self.head.prv = new_head
            self.head = new_head
        self.len += 1
        return

    def addAtTail(self, val: int) -> None:
        if self.len == 0:
            self.head = self.tail = LinkedListNode(val)
        else:
            new_tail = LinkedListNode(val, prv=self.tail)
            self.tail.nxt = new_tail
            self.tail = new_tail
        self.len += 1
        return

    def addAtIndex(self, index: int, val: int) -> None:
        if index <= 0:
            self.addAtHead(val)
            return
        if index == self.len:
            self.addAtTail(val)
            return
        if index > self.len:
            return
        node = self.getNode(index)
        new_node = LinkedListNode(val, nxt=node, prv=node.prv)
        node.prv.nxt = new_node
        node.prv = new_node
        self.len += 1
        return

    def deleteAtIndex(self, index: int) -> None:
        if index < 0 or index >= self.len:
            return
        node = self.getNode(index)
        if node.prv:
            node.prv.nxt = node.nxt
        if node.nxt:
            node.nxt.prv = node.prv
        if index == 0:
            self.head = node.nxt
        if index == self.len - 1:
            self.tail = node.prv
        del node
        self.len -= 1
        return

    def getNode(self, index: int) -> LinkedListNode:
        node = self.head
        for _ in range(index):
            node = node.nxt
        return node

# class MyLinkedList:
#     def __init__(self):
#         """
#         Initialize your data structure here.
#         """
#         self.head = None
#         self.tail = None
#         self.len = 0
#
#     def get(self, index: int) -> int:
#         """
#         Get the value of the index-th node in the linked list. If the index is invalid, return -1.
#         """
#         if index == self.len - 1:  # get列表尾
#             return self.tail.val
#         elif index > self.len - 1 or index < 0:  # index超出范围
#             return -1
#         else:  # get列表头或中间节点
#             NodeGot = self.head
#             IndexGot = 0
#
#         while IndexGot < index:
#             NodeGot = NodeGot.next
#             IndexGot += 1
#
#         return NodeGot.val
#
#     def addAtHead(self, val: int) -> None:
#         """
#         Add a node of value val before the first element of the linked list. After the insertion, the new node will be the first node of the linked list.
#         """
#         if self.head is None:  # 对空列表添加节点
#             NewNode = LinkedListNode(val)
#             self.head = NewNode
#             self.tail = NewNode
#         else:  # 对非空列表添加列表头
#             NewNode = LinkedListNode(val)
#             NewNode.next = self.head
#             self.head.prev = NewNode
#             self.head = NewNode
#
#         self.len += 1
#
#     def addAtTail(self, val: int) -> None:
#         """
#         Append a node of value val to the last element of the linked list.
#         """
#         if self.tail is None:  # 对空列表添加节点
#             NewNode = LinkedListNode(val)
#             self.head = NewNode
#             self.tail = NewNode
#         else:  # 对非空列表添加列表尾
#             NewNode = LinkedListNode(val)
#             NewNode.prev = self.tail
#             self.tail.next = NewNode
#             self.tail = NewNode
#
#         self.len += 1
#
#     def addAtIndex(self, index: int, val: int) -> None:
#         """
#         Add a node of value val before the index-th node in the linked list. If index equals to the length of linked list, the node will be appended to the end of linked list. If index is greater than the length, the node will not be inserted.
#         """
#         if index <= 0:  # 添加列表头
#             self.addAtHead(val)
#         elif index < self.len:  # 添加列表中间节点
#             NewNode = LinkedListNode(val)
#
#             NodeGot = self.head
#             IndexGot = 0
#             while IndexGot < index:
#                 NodeGot = NodeGot.next
#                 IndexGot += 1
#             NodeGot.prev.next = NewNode
#             bridge = NodeGot.prev
#             NodeGot.prev = NewNode
#             NewNode.prev = bridge
#             NewNode.next = NodeGot
#
#             self.len += 1
#         elif index == self.len:  # 添加列表尾
#             self.addAtTail(val)
#         else:  # index大于列表长度不作添加
#             pass
#
#     def deleteAtIndex(self, index: int) -> None:
#         """
#         Delete the index-th node in the linked list, if the index is valid.
#         """
#         if self.len == 0:  # 空列表不作删除
#             pass
#         elif self.len == 1 and index == 0:  # 单一元素列表作删除
#             ListHead = self.head
#             self.head = None
#             self.tail = None
#             del (ListHead)
#
#             self.len = 0
#         elif index > 0 and index < self.len - 1:  # 删除列表中间元素
#             NodeGot = self.head.next
#             IndexGot = 1
#             while IndexGot < index:
#                 NodeGot = NodeGot.next
#                 IndexGot += 1
#             NodeGot.prev.next = NodeGot.next
#             NodeGot.next.prev = NodeGot.prev
#             del (NodeGot)
#
#             self.len -= 1
#         elif index == 0:  # 删除列表头
#             self.deleteHead()
#         elif index == self.len - 1:  # 删除列表尾
#             self.deleteTail()
#         else:  # 其余情况为输入错误，不作删除
#             pass
#
#     def deleteHead(self) -> None:
#         """
#         Delete the head of the linked list.
#         """
#         ListHead = self.head
#         HeadNext = self.head.next
#         self.head = HeadNext
#         HeadNext.prev = None
#         del (ListHead)
#
#         self.len -= 1
#
#     def deleteTail(self) -> None:
#         """
#         Delete the tail of the linked list.
#         """
#         ListTail = self.tail
#         TailPrev = self.tail.prev
#         self.tail = TailPrev
#         TailPrev.next = None
#         del (ListTail)
#
#         self.len -= 1
#
#
# class LinkedListNode:
#     def __init__(self, val: int):
#         """
#         Create the Node of the linked list.
#         """
#         self.val = val
#         self.prev = None
#         self.next = None

# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)
