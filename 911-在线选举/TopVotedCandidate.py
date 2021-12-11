# -*- coding: utf-8 -*-
# LeetCode 911-在线选举

"""
Created on Sat Dec 11 22:14 2021

@author: _Mumu
Environment: py38
"""

from bisect import bisect
from collections import defaultdict
from typing import List


class TopVotedCandidate:
    def __init__(self, persons: List[int], times: List[int]):
        self.leads = []
        self.times = times
        n = len(times)
        votes = defaultdict(int)
        max_votes = 0
        lead_cand = None
        for i in range(n):
            votes[persons[i]] += 1
            if votes[persons[i]] >= max_votes:
                max_votes = votes[persons[i]]
                lead_cand = persons[i]
            self.leads.append(lead_cand)

    def q(self, t: int) -> int:
        return self.leads[bisect(self.times, t) - 1]


# Your TopVotedCandidate object will be instantiated and called as such:
# obj = TopVotedCandidate(persons, times)
# param_1 = obj.q(t)

if __name__ == '__main__':
    t = TopVotedCandidate([0, 1, 1, 0, 0, 1, 0], [0, 5, 10, 15, 20, 25, 30])
    print(t.q(3), t.q(12), t.q(25), t.q(15), t.q(24), t.q(8))
