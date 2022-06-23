# -*- coding: utf-8 -*-
# LeetCode 30-串联所有单词的子串

"""
Created on Thu Jun 23 10:09 2022

@author: _Mumu
Environment: py38
"""

from collections import Counter
from typing import List


class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        cnt = Counter(words)
        k = len(words[0])
        n = len(words)
        return [i for i in range(len(s) - n * k + 1) if Counter(s[i + j * k:i + (j + 1) * k] for j in range(n)) == cnt]

        # cnt = Counter(words)
        # k = len(words[0])
        # n = len(words)
        #
        # def is_start_valid(start: int) -> bool:
        #     if not cnt:
        #         return True
        #     if s[start:start + k] not in cnt:
        #         return False
        #     cnt[s[start:start + k]] -= 1
        #     if cnt[s[start:start + k]] == 0:
        #         cnt.pop(s[start:start + k])
        #     valid = is_start_valid(start + k)
        #     cnt[s[start:start + k]] += 1
        #     return valid
        #
        # ans = []
        # for i in range(len(s) - n * k + 1):
        #     if is_start_valid(i):
        #         ans.append(i)
        # return ans


if __name__ == '__main__':
    s = Solution()
    print(s.findSubstring(s="barfoofoobarthefoobar", words=["bar", "foo", "the"]))
