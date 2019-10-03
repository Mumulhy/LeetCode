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
        if index == self.len - 1:                  # get列表尾
            return self.tail.val
        elif index > self.len - 1 or index < 0:    # index超出范围
            return -1
        else:                                      # get列表头或中间节点
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
        if self.head is None:                 # 对空列表添加节点
            NewNode = LinkedListNode(val)
            self.head = NewNode
            self.tail = NewNode
        else:                                 # 对非空列表添加列表头
            NewNode = LinkedListNode(val)
            NewNode.next = self.head
            self.head.prev = NewNode
            self.head = NewNode

        self.len += 1

    def addAtTail(self, val: int) -> None:
        """
        Append a node of value val to the last element of the linked list.
        """
        if self.tail is None:                 # 对空列表添加节点
            NewNode = LinkedListNode(val)
            self.head = NewNode
            self.tail = NewNode
        else:                                 # 对非空列表添加列表尾
            NewNode = LinkedListNode(val)
            NewNode.prev = self.tail
            self.tail.next = NewNode
            self.tail = NewNode

        self.len += 1

    def addAtIndex(self, index: int, val: int) -> None:
        """
        Add a node of value val before the index-th node in the linked list. If index equals to the length of linked list, the node will be appended to the end of linked list. If index is greater than the length, the node will not be inserted.
        """
        if index <= 0:                          # 添加列表头
            self.addAtHead(val)
        elif index < self.len:                  # 添加列表中间节点
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
        elif index == self.len:                 # 添加列表尾
            self.addAtTail(val)
        else:                                   # index大于列表长度不作添加
            pass

    def deleteAtIndex(self, index: int) -> None:
        """
        Delete the index-th node in the linked list, if the index is valid.
        """
        if self.len == 0:                            # 空列表不作删除
            pass
        elif self.len == 1 and index == 0:           # 单一元素列表作删除
            ListHead = self.head
            self.head = None
            self.tail = None
            del(ListHead)

            self.len = 0
        elif index > 0 and index < self.len - 1:     # 删除列表中间元素
            NodeGot = self.head.next
            IndexGot = 1
            while IndexGot < index:
                NodeGot = NodeGot.next
                IndexGot += 1
            NodeGot.prev.next = NodeGot.next
            NodeGot.next.prev = NodeGot.prev
            del(NodeGot)

            self.len -= 1
        elif index == 0:                             # 删除列表头
            self.deleteHead()
        elif index == self.len - 1:                  # 删除列表尾
            self.deleteTail()
        else:                                        # 其余情况为输入错误，不作删除
            pass

    def deleteHead(self) -> None:
        """
        Delete the head of the linked list.
        """
        ListHead = self.head
        HeadNext = self.head.next
        self.head = HeadNext
        HeadNext.prev = None
        del(ListHead)

        self.len -= 1

    def deleteTail(self) -> None:
        """
        Delete the tail of the linked list.
        """
        ListTail = self.tail
        TailPrev = self.tail.prev
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
