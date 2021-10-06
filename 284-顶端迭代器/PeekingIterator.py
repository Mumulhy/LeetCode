# -*- coding: utf-8 -*-
# LeetCode 284-顶端迭代器

"""
Created on Tues Oct 5 23:00 2021

@author: _Mumu
Environment: py38
"""


# Below is the interface for Iterator, which is already defined for you.
#
# class Iterator:
#     def __init__(self, nums):
#         """
#         Initializes an iterator object to the beginning of a list.
#         :type nums: List[int]
#         """
#
#     def hasNext(self):
#         """
#         Returns true if the iteration has more elements.
#         :rtype: bool
#         """
#
#     def next(self):
#         """
#         Returns the next element in the iteration.
#         :rtype: int
#         """

class PeekingIterator:
    def __init__(self, iterator):
        """
        Initialize your data structure here.
        :type iterator: Iterator
        """
        self.iterator = iterator
        self.pk = None

    def peek(self):
        """
        Returns the next element in the iteration without advancing the iterator.
        :rtype: int
        """
        if self.pk:
            return self.pk
        self.pk = self.iterator.next()
        return self.pk

    def next(self) -> int:
        """
        :rtype: int
        """
        if self.pk:
            res = self.pk
            self.pk = None
            return res
        return self.iterator.next()

    def hasNext(self) -> bool:
        """
        :rtype: bool
        """
        return True if self.pk is not None else self.iterator.hasNext()

# Your PeekingIterator object will be instantiated and called as such:
# iter = PeekingIterator(Iterator(nums))
# while iter.hasNext():
#     val = iter.peek()   # Get the next element but not advance the iterator.
#     iter.next()         # Should return the same value as [val].
