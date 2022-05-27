# -*- coding: utf-8 -*-
# LeetCode 面试题17.11-单词距离

"""
Created on Fri May 27 10:42 2022

@author: _Mumu
Environment: py38
"""

from typing import List


class Solution:
    def findClosest(self, words: List[str], word1: str, word2: str) -> int:
        last_pos = {}
        ans = 100000
        for i, word in enumerate(words):
            if word != word1 and word != word2:
                continue
            if word1 not in last_pos or word2 not in last_pos:
                if last_pos and word not in last_pos:
                    ans = min(ans, i - list(last_pos.values())[0])
                    if ans == 1:
                        return ans
                last_pos[word] = i
                continue
            if word == word1:
                ans = min(ans, i - last_pos[word2])
            if word == word2:
                ans = min(ans, i - last_pos[word1])
            if ans == 1:
                return ans
            last_pos[word] = i
        return ans


if __name__ == '__main__':
    s = Solution()
    print(s.findClosest(words=["I", "am", "a", "student", "from", "a", "university", "in", "a", "city"],
                        word1="a",
                        word2="student"))
