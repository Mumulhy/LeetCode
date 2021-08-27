# -*- coding: utf-8 -*-
# LeetCode 295-数据流的中位数

"""
Created on Fri Aug 27 14:12 2021

@author: _Mumu
Environment: py38
"""

# from sortedcontainers import SortedList
from heapq import heappush, heappushpop


class MedianFinder:
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.minHeapLarge = []
        self.maxHeapSmall = []

    def addNum(self, num: int) -> None:
        if len(self.minHeapLarge) == len(self.maxHeapSmall):
            heappush(self.minHeapLarge, -heappushpop(self.maxHeapSmall, -num))
        else:
            heappush(self.maxHeapSmall, -heappushpop(self.minHeapLarge, num))

    def findMedian(self) -> float:
        if len(self.minHeapLarge) == len(self.maxHeapSmall):
            return (self.minHeapLarge[0] - self.maxHeapSmall[0]) / 2
        else:
            return self.minHeapLarge[0]

    # def __init__(self):
    #     """
    #     initialize your data structure here.
    #     """
    #     self.nums = SortedList()
    #     self.left, self.right = -1, 0
    #     self.n = 0
    #
    # def addNum(self, num: int) -> None:
    #     self.nums.add(num)
    #     self.n += 1
    #     if self.left == -1:
    #         self.left = 0
    #     else:
    #         if self.n & 1 == 0:
    #             self.right += 1
    #         else:
    #             self.left = self.right
    #     return
    #
    # def findMedian(self) -> float:
    #     return (self.nums[self.left] + self.nums[self.right]) / 2


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()

if __name__ == '__main__':
    m = MedianFinder()
    m.addNum(-1)
    m.addNum(-2)
    print(m.findMedian())
    m.addNum(-3)
    print(m.findMedian())
