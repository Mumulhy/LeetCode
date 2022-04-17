# -*- coding: utf-8 -*-
# LeetCode 819-最常见的单词

"""
Created on Sun Apr 17 15:33 2022

@author: _Mumu
Environment: py38
"""

from collections import defaultdict
from typing import List


class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        banned = set(banned)
        cnt = defaultdict(int)
        max_times = 0
        ans = ''
        curr_word = ''
        for ch in paragraph:
            if 'a' <= ch <= 'z':
                curr_word += ch
            elif 'A' <= ch <= 'Z':
                curr_word += chr(ord(ch) ^ 32)
            else:
                if curr_word and curr_word not in banned:
                    cnt[curr_word] += 1
                    if cnt[curr_word] > max_times:
                        max_times = cnt[curr_word]
                        ans = curr_word
                curr_word = ''
        if curr_word and curr_word not in banned:
            cnt[curr_word] += 1
            if cnt[curr_word] > max_times:
                return curr_word
        return ans


if __name__ == '__main__':
    s = Solution()
    print(s.mostCommonWord("Bob hit a ball, the hit BALL flew far after it was hit.", ["hit"]))
