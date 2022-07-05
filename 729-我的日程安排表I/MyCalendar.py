# -*- coding: utf-8 -*-
# LeetCode 729-我的日程安排表I

"""
Created on Tues Jul 5 12:28 2022

@author: _Mumu
Environment: py38
"""

from bisect import bisect_left


class MyCalendar:
    def __init__(self):
        self.calender = []

    def book(self, start: int, end: int) -> bool:
        rep = []
        idx_s = bisect_left(self.calender, start)
        idx_e = bisect_left(self.calender, end)
        if idx_e - idx_s > 2:
            return False
        if idx_s & 1 == 0:
            if idx_e - idx_s == 2 or (idx_s < len(self.calender) and self.calender[idx_s] == start):
                return False
            rep.append(start)
        else:
            if not (idx_s < len(self.calender) and self.calender[idx_s] == start):
                return False
        if idx_e & 1 == 1:
            return False
        if idx_e < len(self.calender) and self.calender[idx_e] == end:
            idx_e += 1
        else:
            rep.append(end)
        self.calender[idx_s:idx_e] = rep
        return True

# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(start,end)
