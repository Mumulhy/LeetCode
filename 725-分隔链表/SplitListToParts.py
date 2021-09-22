# -*- coding: utf-8 -*-
# LeetCode 725-分隔链表

"""
Created on Wed Sept 21 21:37 2021

@author: _Mumu
Environment: py38
"""

from typing import List


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def splitListToParts(self, head: ListNode, k: int) -> List[ListNode]:
        node = head
        n = 0
        while node:
            n += 1
            node = node.next
        nModK = n % k
        n //= k
        node = head
        parts = []
        for _ in range(nModK):
            parts.append(node)
            for _ in range(n):
                node = node.next
            now = node
            node = node.next
            now.next = None
        for _ in range(k - nModK):
            parts.append(node)
            if not node:
                continue
            for _ in range(n - 1):
                node = node.next
            now = node
            node = node.next
            now.next = None
        return parts


if __name__ == '__main__':
    s = Solution()
    head = ListNode(1,
                    ListNode(2,
                             ListNode(3,
                                      ListNode(4,
                                               ListNode(5,
                                                        ListNode(6,
                                                                 ListNode(7,
                                                                          ListNode(8,
                                                                                   ListNode(9,
                                                                                            ListNode(10))))))))))
    parts = s.splitListToParts(head, 4)
    print(len(parts))
    for node in parts:
        if node:
            print(node.val, end=' ')
        else:
            print('#', end=' ')
