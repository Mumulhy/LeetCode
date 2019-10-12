# -*- coding: utf-8 -*-
# LeetCode 2-两数相加

"""
Created on Sat Oct 12 08:17 2019

@author: _Mumu
Environment: py37
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:

        forward = False

        head = ListNode(l1.val + l2.val)             # 处理个位
        if head.val >= 10:
            head.val -= 10
            forward = True

        l1 = l1.next
        l2 = l2.next
        l3 = head

        while l1 and l2:                             # 处理除个位以外的共有位数
            l3.next = ListNode(l1.val + l2.val)
            l3 = l3.next
            
            if forward == True:
                l3.val += 1
            
            if l3.val >= 10:
                l3.val -= 10
                forward = True
            else:
                forward = False
            
            l1 = l1.next
            l2 = l2.next

        while l1:                                    # 处理非共有的位数（即某个数比另一个数更长的部分）
            l3.next = ListNode(l1.val)
            l3 = l3.next

            if forward == True:
                l3.val += 1
            
            if l3.val >= 10:
                l3.val -= 10
                forward = True
            else:
                forward = False
            
            l1 = l1.next

        while l2:
            l3.next = ListNode(l2.val)
            l3 = l3.next
            
            if forward == True:
                l3.val += 1
            
            if l3.val >= 10:
                l3.val -= 10
                forward = True
            else:
                forward = False
            
            l2 = l2.next

        if forward == True:                          # 处理最高位相加进位的问题
            l3.next = ListNode(1)

        return head

        # 以下为最快算法

        # carry=0
        # head=ListNode(0)
        # cur=head
        # while(l1 or l2):
        #     x=l1.val if l1 else 0
        #     y=l2.val if l2 else 0
        #     s=carry+x+y
        #     carry=s//10
        #     cur.next=ListNode(s%10)
        #     cur=cur.next
        #     if(l1!=None):   l1=l1.next
        #     if(l2!=None):   l2=l2.next
        # if(carry>0):    cur.next=ListNode(1)
        # return head.next