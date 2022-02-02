# -*- coding: utf-8 -*-
# LeetCode 2000-反转单词前缀

"""
Created on Wed Feb 2 20:36 2022

@author: _Mumu
Environment: py38
"""


class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        idx = -1
        for i, c in enumerate(word):
            if c == ch:
                idx = i
                break
        return word if idx == -1 else word[0:idx + 1][::-1] + word[idx + 1:]


if __name__ == '__main__':
    s = Solution()
    print(s.reversePrefix(word="abcdefd", ch="d"))
