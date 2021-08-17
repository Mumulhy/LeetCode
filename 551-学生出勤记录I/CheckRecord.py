# -*- coding: utf-8 -*-
# LeetCode 551-学生出勤记录I

"""
Created on Tues Aug 17 22:05 2021

@author: _Mumu
Environment: py38
"""


class Solution:
    def checkRecord(self, s: str) -> bool:
        if s.count('A') >= 2 or 'LLL' in s:
            return False
        else:
            return True


if __name__ == '__main__':
    s = Solution()
    print(s.checkRecord('PPALLLLA'))
