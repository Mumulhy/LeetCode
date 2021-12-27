# -*- coding: utf-8 -*-
# LeetCode 1705-吃苹果的最大数目

"""
Created on Fri Dec 24 11:04 2021

@author: _Mumu
Environment: py38
"""

# from sortedcontainers import SortedDict
from heapq import heappush, heappop
from typing import List


class Solution:
    def eatenApples(self, apples: List[int], days: List[int]) -> int:
        ans = 0
        unavailable_days = []
        last_day = len(apples)
        for i in range(last_day):
            while unavailable_days and unavailable_days[0][0] <= i:
                heappop(unavailable_days)
            if apples[i] != 0:
                heappush(unavailable_days, [i + days[i], apples[i]])
            if unavailable_days:
                if unavailable_days[0][1] == 1:
                    heappop(unavailable_days)
                else:
                    unavailable_days[0][1] -= 1
                ans += 1
        while unavailable_days:
            while unavailable_days and unavailable_days[0][0] <= last_day:
                heappop(unavailable_days)
            if not unavailable_days:
                break
            ans += min(unavailable_days[0][1], unavailable_days[0][0] - last_day)
            last_day = min(last_day + unavailable_days[0][1], unavailable_days[0][0])
            heappop(unavailable_days)
        return ans

        # ans = 0
        # unavailable_days = SortedDict()
        # for i, (apple, day) in enumerate(zip(apples, days)):
        #     for u in unavailable_days:
        #         if u <= i:
        #             unavailable_days.pop(u)
        #         else:
        #             break
        #     if apple != 0:
        #         curr_unavailable_day = i + day
        #         if curr_unavailable_day in unavailable_days:
        #             unavailable_days[curr_unavailable_day] += apple
        #         else:
        #             unavailable_days[curr_unavailable_day] = apple
        #     for u in unavailable_days:
        #         unavailable_days[u] -= 1
        #         if unavailable_days[u] == 0:
        #             unavailable_days.pop(u)
        #         ans += 1
        #         break
        # last_day = len(apples)
        # for u, apple in unavailable_days.items():
        #     ans += min(apple, u - last_day)
        #     last_day = min(last_day + apple, u)
        # return ans
