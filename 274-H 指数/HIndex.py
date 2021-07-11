# -*- coding: utf-8 -*-
# LeetCode 274-H 指数

"""
Created on Sun Jul 11 20:16 2021

@author: _Mumu
Environment: py38
"""

from typing import List


class Solution:
    def hIndex(self, citations: List[int]) -> int:
        count_citations = {}
        for citation in citations:
            if citation in count_citations:
                count_citations[citation] += 1
            else:
                count_citations[citation] = 1
        times = 0
        for citation in sorted(count_citations, reverse=True):
            if times > citation:
                return times
            times += count_citations[citation]
            if times > citation >= times - count_citations[citation]:
                return citation
        return times

if __name__ == '__main__':
    s = Solution()
    print(s.hIndex([100,100,1,1]))