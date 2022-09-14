# -*- coding: utf-8 -*-
# LeetCode 1619-删除某些元素后的数组均值

"""
Created on Wed Sept 14 10:31 2022

@author: _Mumu
Environment: py38
"""

from heapq import heappush, heappop
from typing import List


class Solution:
    def trimMean(self, arr: List[int]) -> float:
        k = len(arr) // 20
        largest = []
        smallest = []
        for num in arr[:k]:
            heappush(largest, -num)
            heappush(smallest, num)
        for num in arr[k:]:
            heappush(largest, -num)
            heappush(smallest, num)
            heappop(largest)
            heappop(smallest)
        return (sum(arr) + sum(largest) - sum(smallest)) / (18 * k)


if __name__ == '__main__':
    s = Solution()
    print(s.trimMean([6, 0, 7, 0, 7, 5, 7, 8, 3, 4, 0, 7, 8, 1, 6, 8, 1, 1, 2, 4, 8, 1, 9, 5, 4, 3, 8, 5, 10, 8, 6, 6,
                      1, 0, 6, 10, 8, 2, 3, 4]))
