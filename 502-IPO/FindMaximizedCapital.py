# -*- coding: utf-8 -*-
# LeetCode 502-IPO

"""
Created on Wed Sept 8 20:47 2021

@author: _Mumu
Environment: py38
"""

from heapq import heappush, heappop, nlargest
from typing import List


class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        if w >= max(capital):
            return w + sum(nlargest(k, profits))

        profitsHeap = []
        i = 0
        n = len(capital)
        arr = [(capital[j], profits[j]) for j in range(n)]
        arr.sort(key=lambda x: x[0])
        for _ in range(k):
            while i < n and arr[i][0] <= w:
                heappush(profitsHeap, -arr[i][1])
                i += 1
            if not profitsHeap:
                return w
            w -= heappop(profitsHeap)
        return w

        # profitsHeap = []
        # i = 0
        # n = len(capital)
        # capital, profits = (list(t) for t in zip(*sorted(zip(capital, profits))))
        # for _ in range(k):
        #     while i < n and capital[i] <= w:
        #         heappush(profitsHeap, -profits[i])
        #         i += 1
        #     if not profitsHeap:
        #         return w
        #     w -= heappop(profitsHeap)
        # return w


if __name__ == '__main__':
    s = Solution()
    print(s.findMaximizedCapital(k=3, w=3, profits=[1, 2, 3], capital=[1, 1, 2]))
