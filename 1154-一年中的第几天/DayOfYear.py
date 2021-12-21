# -*- coding: utf-8 -*-
# LeetCode 1154-一年中的第几天

"""
Created on Tues Dec 21 10:28 2021

@author: _Mumu
Environment: py38
"""


class Solution:
    def __init__(self):
        self.common_year = {2: 59, 3: 90, 4: 120, 5: 151, 6: 181, 7: 212, 8: 243, 9: 273, 10: 304, 11: 334}
        self.leap_year = {2: 60, 3: 91, 4: 121, 5: 152, 6: 182, 7: 213, 8: 244, 9: 274, 10: 305, 11: 335}

    def dayOfYear(self, date: str) -> int:
        m = int(date[5:7])
        d = int(date[-2:])
        if m <= 2:
            return d if m == 1 else 31 + d
        y = int(date[:4])
        is_leap_year = y % 4 == 0 and (y % 100 != 0 or y % 400 == 0)
        return self.leap_year[m - 1] + d if is_leap_year else self.common_year[m - 1] + d


if __name__ == '__main__':
    s = Solution()
    print(s.dayOfYear('1900-03-01'))
