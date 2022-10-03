# -*- coding: utf-8 -*-
# LeetCode 1784-检查二进制字符串字段

"""
Created on Mon Oct 3 13:12 2022

@author: _Mumu
Environment: py38
"""


class Solution:
    def checkOnesSegment(self, s: str) -> bool:
        flag = False
        for ch in s:
            if ch == '0':
                flag = True
            else:
                if flag:
                    return False
        return True


if __name__ == '__main__':
    s = Solution()
    print(s.checkOnesSegment("110"))
