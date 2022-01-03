# -*- coding: utf-8 -*-
# LeetCode 1185-一周中的第几天

"""
Created on Mon Jan 3 10:23 2022

@author: _Mumu
Environment: py38
"""


class Solution:
    def dayOfTheWeek(self, day: int, month: int, year: int) -> str:
        week = ["Thursday", "Friday", "Saturday", "Sunday", "Monday", "Tuesday", "Wednesday"]
        idx = 0
        # for y in range(1971, year):
        #     idx += 2 if y % 4 == 0 and y != 2100 else 1
        idx += year - 1971 + (year - 1969) // 4
        idx %= 7
        if year % 4 == 0 and year != 2100:
            months = [0, 0, 3, 4, 0, 2, 5, 0, 3, 6, 1, 4, 6]
        else:
            months = [0, 0, 3, 3, 6, 1, 4, 6, 2, 5, 0, 3, 5]
        idx += months[month] + day
        idx %= 7
        return week[idx]


if __name__ == '__main__':
    s = Solution()
    print(s.dayOfTheWeek(15, 12, 2021))
