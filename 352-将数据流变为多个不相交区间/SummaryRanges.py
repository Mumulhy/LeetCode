# -*- coding: utf-8 -*-
# LeetCode 352-将数据流变为多个不相交区间

"""
Created on Sat Oct 9 19:45 2021

@author: _Mumu
Environment: py38
"""

from sortedcontainers import SortedDict
from typing import List


class SummaryRanges:
    def __init__(self):
        self.intervals = SortedDict()

    def addNum(self, val: int) -> None:
        intervals_ = self.intervals
        keys_ = self.intervals.keys()
        values_ = self.intervals.values()
        n = len(intervals_)

        interval1 = intervals_.bisect_right(val)
        interval0 = n if interval1 == 0 else interval1 - 1

        if interval0 != n and keys_[interval0] <= val <= values_[interval0]:
            return
        left_aside = interval0 != n and values_[interval0] + 1 == val
        right_aside = interval1 != n and keys_[interval1] - 1 == val
        if left_aside and right_aside:
            left, right = keys_[interval0], values_[interval1]
            intervals_.popitem(interval1)
            intervals_.popitem(interval0)
            intervals_[left] = right
        elif left_aside:
            intervals_[keys_[interval0]] += 1
        elif right_aside:
            right = values_[interval1]
            intervals_.popitem(interval1)
            intervals_[val] = right
        else:
            intervals_[val] = val
        return

    def getIntervals(self) -> List[List[int]]:
        return list(self.intervals.items())

# Your SummaryRanges object will be instantiated and called as such:
# obj = SummaryRanges()
# obj.addNum(val)
# param_2 = obj.getIntervals()
