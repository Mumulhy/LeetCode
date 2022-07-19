# -*- coding: utf-8 -*-
# LeetCode 731-我的日程安排表II

"""
Created on Tues Jul 19 10:05 2022

@author: _Mumu
Environment: py38
"""

from sortedcontainers import SortedDict


class MyCalendarTwo:
    def __init__(self):
        self.d = SortedDict()

    def book(self, start: int, end: int) -> int:
        self.d[start] = self.d.get(start, 0) + 1
        self.d[end] = self.d.get(end, 0) - 1
        max_book = 0
        for diff in self.d.values():
            max_book += diff
            if max_book > 2:
                self.d[start] = self.d.get(start, 0) - 1
                self.d[end] = self.d.get(end, 0) + 1
                return False
        return True

# Your MyCalendarTwo object will be instantiated and called as such:
# obj = MyCalendarTwo()
# param_1 = obj.book(start,end)
