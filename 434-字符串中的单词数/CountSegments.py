# -*- coding: utf-8 -*-
# LeetCode 434-字符串中的单词数

"""
Created on Thu Oct 7 20:50 2021

@author: _Mumu
Environment: py38
"""


class Solution:
    def countSegments(self, s: str) -> int:
        if not s:
            return 0
        words = 0
        if s[0] != ' ':
            words += 1
        for i in range(1, len(s)):
            if s[i - 1] == ' ' and s[i] != ' ':
                words += 1
        return words


if __name__ == '__main__':
    s = Solution()
    print(s.countSegments("Hello, my name is John"))
