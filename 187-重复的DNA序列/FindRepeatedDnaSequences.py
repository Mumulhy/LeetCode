# -*- coding: utf-8 -*-
# LeetCode 187-重复的DNA序列

"""
Created on Fri Oct 8 21:45 2021

@author: _Mumu
Environment: py38
"""

from typing import List


class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        n = len(s)
        if n <= 10:
            return []
        binDna = {'A': 0, 'C': 1, 'G': 2, 'T': 3}
        repeatedSeq = []
        subDnaSeq = set()
        x = 0
        for ch in s[0:9]:
            x = (x << 2) | binDna[ch]
        for i in range(9, n):
            x = ((x << 2) | binDna[s[i]]) & ((1 << 20) - 1)
            if x in subDnaSeq:
                if s[i - 9:i + 1] not in repeatedSeq:
                    repeatedSeq.append(s[i - 9:i + 1])
            else:
                subDnaSeq.add(x)
        return repeatedSeq

        # if len(s) <= 10:
        #     return []
        # repeatedSeq = []
        # subDnaSeq = set()
        # for i in range(10, len(s) + 1):
        #     if s[i - 10:i] in subDnaSeq:
        #         if s[i - 10:i] not in repeatedSeq:
        #             repeatedSeq.append(s[i - 10:i])
        #     else:
        #         subDnaSeq.add(s[i - 10:i])
        # return repeatedSeq


if __name__ == '__main__':
    s = Solution()
    print(s.findRepeatedDnaSequences("AAAAAAAAAAAAAAA"))
