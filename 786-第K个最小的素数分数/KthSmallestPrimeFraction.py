# -*- coding: utf-8 -*-
# LeetCode 786-第K个最小的素数分数

"""
Created on Mon Nov 29 20:32 2021

@author: _Mumu
Environment: py38
"""

# from heapq import heapify, heappop, heappush
from typing import List


# class Frac:
#     def __init__(self, idx: int, idy: int, x: int, y: int):
#         self.idx, self.idy = idx, idy
#         self.x, self.y = x, y
#
#     def __lt__(self, other: 'Frac') -> bool:
#         return self.x * other.y < self.y * other.x


class Solution:
    def kthSmallestPrimeFraction(self, arr: List[int], k: int) -> List[int]:
        n = len(arr)
        left, right = 0.0, 1.0
        while True:
            mid = (left + right) / 2
            i, count = 0, 0
            x, y = 0, 1
            for j in range(1, n):
                while arr[i] / arr[j] < mid:
                    if arr[i] * y > arr[j] * x:
                        x, y = arr[i], arr[j]
                    i += 1
                count += i
            if count == k:
                return [x, y]
            if count > k:
                right = mid
            else:
                left = mid

        # n = len(arr)
        # q = [Frac(0, i, arr[0], arr[i]) for i in range(1, n)]
        # heapify(q)
        # for _ in range(k - 1):
        #     frac = heappop(q)
        #     if frac.idx + 1 < frac.idy:
        #         heappush(q, Frac(frac.idx + 1, frac.idy, arr[frac.idx + 1], arr[frac.idy]))
        # return [q[0].x, q[0].y]

        # return sorted([[arr[i], arr[j]] for i in range(len(arr)) for j in range(i + 1, len(arr))],
        #               key=lambda x: x[0] / x[1])[k - 1]


if __name__ == '__main__':
    s = Solution()
    print(s.kthSmallestPrimeFraction(arr=[1, 2, 3, 5], k=3))
