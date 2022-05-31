# -*- coding: utf-8 -*-
# LeetCode 剑指OfferII114-外星文字典

"""
Created on Tues May 31 10:01 2022

@author: _Mumu
Environment: py38
"""

from collections import defaultdict
from more_itertools import pairwise
from typing import List


class Solution:
    def alienOrder(self, words: List[str]) -> str:
        g = defaultdict(list)
        in_deg = {c: 0 for c in words[0]}
        for s, t in pairwise(words):
            for c in t:
                in_deg.setdefault(c, 0)
            same = True
            for u, v in zip(s, t):
                if u != v:
                    g[u].append(v)
                    in_deg[v] += 1
                    same = False
                    break
            if same and len(s) > len(t):
                return ''
        q = [u for u, d in in_deg.items() if d == 0]
        for u in q:
            for v in g[u]:
                in_deg[v] -= 1
                if in_deg[v] == 0:
                    q.append(v)
        return ''.join(q) if len(q) == len(in_deg) else ''


if __name__ == '__main__':
    s = Solution()
    print(s.alienOrder(["wrt", "wrf", "er", "ett", "rftt"]))
