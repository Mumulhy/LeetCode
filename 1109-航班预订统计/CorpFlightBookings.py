# -*- coding: utf-8 -*-
# LeetCode 1109-航班预订统计

"""
Created on Tues Aug 31 17:32 2021

@author: _Mumu
Environment: py38
"""

from typing import List


class Solution:
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
        flights = [0] * n
        for first, last, seats in bookings:
            flights[first - 1] += seats
            if last < n:
                flights[last] -= seats
        for i in range(1, n):
            flights[i] += flights[i - 1]
        return flights


if __name__ == '__main__':
    s = Solution()
    print(s.corpFlightBookings(bookings=[[1, 2, 10], [2, 3, 20], [2, 5, 25]], n=5))
