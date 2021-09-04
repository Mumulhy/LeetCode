# -*- coding: utf-8 -*-
# LeetCode 剑指Offer22-链表中倒数第k个节点

"""
Created on Thur Sept 2 23:41 2021

@author: _Mumu
Environment: py38
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def getKthFromEnd(self, head: ListNode, k: int) -> ListNode:
        node = head
        kthFromNode = head
        for _ in range(k):
            node = node.next
        while node:
            node = node.next
            kthFromNode = kthFromNode.next
        return kthFromNode


if __name__ == '__main__':
    s = Solution()
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)
    head.next.next.next = ListNode(4)
    head.next.next.next.next = ListNode(5)
    print(s.getKthFromEnd(head, 2).val)
