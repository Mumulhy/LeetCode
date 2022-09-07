# -*- coding: utf-8 -*-
# LeetCode 1592-重新排列单词间的空格

"""
Created on Wed Sept 7 10:37 2022

@author: _Mumu
Environment: py38
"""


class Solution:
    def reorderSpaces(self, text: str) -> str:
        spaces = text.count(' ')
        text = text.strip().replace('  ', ' ').split()
        if len(text) == 1:
            return text[0] + ' ' * spaces
        k, left = divmod(spaces, len(text) - 1)
        return (' ' * k).join(text) + ' ' * left


if __name__ == '__main__':
    s = Solution()
    print(s.reorderSpaces("  walks  udp package   into  bar a"))
