# -*- coding: utf-8 -*-
# LeetCode 806-写字符串需要的行数

"""
Created on Tues Apr 12 13:51 2022

@author: _Mumu
Environment: py38
"""

from typing import List


class Solution:
    def numberOfLines(self, widths: List[int], s: str) -> List[int]:
        lines = 1
        curr_line = 0
        for letter in s:
            if curr_line + widths[ord(letter) - ord('a')] > 100:
                lines += 1
                curr_line = widths[ord(letter) - ord('a')]
            else:
                curr_line += widths[ord(letter) - ord('a')]
        return [lines, curr_line]


if __name__ == '__main__':
    s = Solution()
    print(s.numberOfLines(widths=[10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10,
                                  10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10],
                          s="abcdefghijklmnopqrstuvwxyz"))
