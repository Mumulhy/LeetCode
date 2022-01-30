# -*- coding: utf-8 -*-
# LeetCode 884-两句话中的不常见单词

"""
Created on Sun Jan 30 11:35 2022

@author: _Mumu
Environment: py38
"""

from collections import Counter
from typing import List


class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        cnt = Counter(s1.split()) + Counter(s2.split())
        ans = []
        for word in cnt:
            if cnt[word] == 1:
                ans.append(word)
        return ans

        # cnt1 = Counter(s1.split(' '))
        # cnt2 = Counter(s2.split(' '))
        # ans = []
        # for word1 in cnt1:
        #     if cnt1[word1] == 1 and word1 not in cnt2:
        #         ans.append(word1)
        # for word2 in cnt2:
        #     if cnt2[word2] == 1 and word2 not in cnt1:
        #         ans.append(word2)
        # return ans


if __name__ == '__main__':
    s = Solution()
    print(s.uncommonFromSentences(s1="this apple is sweet", s2="this apple is sour"))
