# -*- coding: utf-8 -*-
# LeetCode 1736-替换隐藏数字得到的最晚时间

"""
Created on Sat Jul 24 10:53 2021

@author: _Mumu
Environment: py38
"""


class Solution:
    def maximumTime(self, time: str) -> str:
        time_split = list(time)
        if time_split[0] == '?':
            if time_split[1] in '0123?':
                time_split[0] = '2'
            else:
                time_split[0] = '1'
        if time_split[1] == '?':
            if time_split[0] == '2':
                time_split[1] = '3'
            else:
                time_split[1] = '9'
        if time_split[3] == '?':
            time_split[3] = '5'
        if time_split[4] == '?':
            time_split[4] = '9'
        return ''.join(time_split)


if __name__ == '__main__':
    s = Solution()
    print(s.maximumTime('0?:0?'))
