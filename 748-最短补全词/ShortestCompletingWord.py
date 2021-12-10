# -*- coding: utf-8 -*-
# LeetCode 748-最短补全词

"""
Created on Fri Dec 10 21:27 2021

@author: _Mumu
Environment: py38
"""

from collections import Counter
from typing import List


class Solution:
    def shortestCompletingWord(self, licensePlate: str, words: List[str]) -> str:
        cnt = Counter(ch.lower() for ch in licensePlate if ch.isalpha())
        return min((word for word in words if not cnt - Counter(word)), key=len)

        # cnt = Counter()
        # for s in licensePlate:
        #     if '0' <= s <= '9' or s == ' ':
        #         continue
        #     cnt[s.lower()] += 1
        # ans = ''
        # ans_len = 0
        # for word in words:
        #     word_cnt = Counter(word)
        #     word_len = len(word)
        #     if (ans == '' or word_len < ans_len) and cnt & word_cnt == cnt:
        #         ans = word
        #         ans_len = word_len
        # return ans


if __name__ == '__main__':
    s = Solution()
    print(s.shortestCompletingWord(licensePlate="iMSlpe4",
                                   words=["claim", "consumer", "student", "camera", "public",
                                          "never", "wonder", "simple", "thought", "use"]))
