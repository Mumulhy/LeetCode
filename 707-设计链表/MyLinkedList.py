# -*- coding: utf-8 -*-
# LeetCode 707-设计链表

"""
Created on Wed Oct 2 00:07 2019

@author: _Mumu
Environment: py37
"""

class MyLinkedList:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.head = None
        self.tail = None
        self.len = 0

    def get(self, index: int) -> int:
        """
        Get the value of the index-th node in the linked list. If the index is invalid, return -1.
        """
        if index == self.len - 1:
            return self.tail.val
        elif index > self.len - 1 or index < 0:
            return -1
        else:
            NodeGot = self.head
            IndexGot = 0

        while IndexGot < index:
            NodeGot = NodeGot.next
            IndexGot += 1

        return NodeGot.val

    def addAtHead(self, val: int) -> None:
        """
        Add a node of value val before the first element of the linked list. After the insertion, the new node will be the first node of the linked list.
        """
        if self.head is None:
            NewNode = LinkedListNode(val)
            self.head = NewNode
            self.tail = NewNode
        else:
            NewNode = LinkedListNode(val)
            NewNode.next = self.head
            self.head.prev = NewNode
            self.head = NewNode

        self.len += 1

    def addAtTail(self, val: int) -> None:
        """
        Append a node of value val to the last element of the linked list.
        """
        if self.tail is None:
            self.head = LinkedListNode(val)
            self.tail = LinkedListNode(val)
        else:
            NewNode = LinkedListNode(val)
            NewNode.prev = self.tail
            self.tail.next = NewNode
            self.tail = NewNode

        self.len += 1

    def addAtIndex(self, index: int, val: int) -> None:
        """
        Add a node of value val before the index-th node in the linked list. If index equals to the length of linked list, the node will be appended to the end of linked list. If index is greater than the length, the node will not be inserted.
        """
        if index <= 0:
            self.addAtHead(val)
        elif index < self.len:
            NewNode = LinkedListNode(val)

            NodeGot = self.head
            IndexGot = 0
            while IndexGot < index:
                NodeGot = NodeGot.next
                IndexGot += 1
            NodeGot.prev.next = NewNode
            bridge = NodeGot.prev
            NodeGot.prev = NewNode
            NewNode.prev = bridge
            NewNode.next = NodeGot

            self.len += 1
        elif index == self.len:
            self.addAtTail(val)
        else:
            pass

    def deleteAtIndex(self, index: int) -> None:
        """
        Delete the index-th node in the linked list, if the index is valid.
        """
        if index > 0 and index < self.len - 1:
            NodeGot = self.head.next
            IndexGot = 1
            while IndexGot < index:
                NodeGot = NodeGot.next
                IndexGot += 1
            NodeGot.prev.next = NodeGot.next
            NodeGot.next.prev = NodeGot.prev
            del(NodeGot)

            self.len -= 1
        elif index == 0:
            self.deleteHead()
        elif index == self.len - 1:
            self.deleteTail()
        else:
            pass

    def deleteHead(self) -> None:
        """
        Delete the head of the linked list.
        """
        if self.head is None:
            pass
        elif self.len == 1:
            ListHead = self.head
            self.head = None
            self.tail = None
            del(ListHead)
        else:
            ListHead = self.head
            if ListHead.next is None:
                self.head = None
                del(ListHead)
            else:
                HeadNext = ListHead.next
                self.head = HeadNext
                HeadNext.prev = None
                del(ListHead)

            self.len -= 1

    def deleteTail(self) -> None:
        """
        Delete the tail of the linked list.
        """
        if self.tail is None:
            pass
        elif self.len == 1:
            ListTail = self.tail
            self.head = None
            self.tail = None
            del(ListHead)
        else:
            ListTail = self.tail
            if ListTail.prev is None:
                self.tail = None
                del(ListTail)
            else:
                TailPrev = ListTail.prev
                self.tail = TailPrev
                TailPrev.next = None
                del(ListTail)

            self.len -= 1



class LinkedListNode:

    def __init__(self, val: int):
        """
        Create the Node of the linked list.
        """
        self.val = val
        self.prev = None
        self.next = None



# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)
