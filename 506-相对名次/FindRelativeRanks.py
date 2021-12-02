# -*- coding: utf-8 -*-
# LeetCode 506-相对名次

"""
Created on Thu Dec 2 14:09 2021

@author: _Mumu
Environment: py38
"""

from typing import List


class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        medals = ['Gold Medal', 'Silver Medal', 'Bronze Medal']
        n = len(score)
        if n == 1:
            return medals[:1]
        if n == 2:
            return medals[:2] if score[0] > score[1] else medals[:2][::-1]
        sorted_score = sorted(score, reverse=True)
        rank = {sc: str(i + 1) for i, sc in enumerate(sorted_score)}
        for i in range(3):
            rank[sorted_score[i]] = medals[i]
        return [rank[sc] for sc in score]


if __name__ == '__main__':
    s = Solution()
    print(s.findRelativeRanks([10, 3, 8, 9, 4]))
