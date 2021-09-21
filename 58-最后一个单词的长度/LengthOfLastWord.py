# -*- coding: utf-8 -*-
# LeetCode 58-最后一个单词的长度

"""
Created on Tues Sept 21 14:19 2021

@author: _Mumu
Environment: py38
"""


class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        return len(s.split()[-1])

        # length = 0
        # for ch in s[::-1]:
        #     if ch == ' ':
        #         if length:
        #             break
        #     else:
        #         length += 1
        # return length


if __name__ == '__main__':
    s = Solution()
    print(s.lengthOfLastWord("luffy is still joyboy"))
