# -*- coding: utf-8 -*-
# LeetCode 2483-商店的最少代价

"""
Created on Fri Dec 26 07:14 2025

@author: _Mumu
Environment: py38
"""


class Solution:
    def bestClosingTime(self, customers: str) -> int:
        num_y = customers.count('Y')
        closing_time = 0
        curr_cost = num_y
        best_cost = num_y
        for i, ch in enumerate(customers):
            if ch == 'Y':
                curr_cost -= 1
            else:
                curr_cost += 1
            if curr_cost < best_cost:
                best_cost = curr_cost
                closing_time = i + 1
        return closing_time
