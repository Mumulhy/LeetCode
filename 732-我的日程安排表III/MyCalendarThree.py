# -*- coding: utf-8 -*-
# LeetCode 732-我的日程安排表III

"""
Created on Mon Jun 6 09:59 2022

@author: _Mumu
Environment: py38
"""

from sortedcontainers import SortedDict


class MyCalendarThree:
    def __init__(self):
        self.d = SortedDict()

    def book(self, start: int, end: int) -> int:
        self.d[start] = self.d.setdefault(start, 0) + 1
        self.d[end] = self.d.setdefault(end, 0) - 1
        ans = max_book = 0
        for diff in self.d.values():
            max_book += diff
            ans = max(ans, max_book)
        return ans

# Your MyCalendarThree object will be instantiated and called as such:
# obj = MyCalendarThree()
# param_1 = obj.book(start,end)
