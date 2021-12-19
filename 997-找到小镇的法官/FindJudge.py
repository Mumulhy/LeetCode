# -*- coding: utf-8 -*-
# LeetCode 997-找到小镇的法官

"""
Created on Sun Dec 19 10:47 2021

@author: _Mumu
Environment: py38
"""

# from collections import defaultdict
from collections import Counter
from typing import List


class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        out_degrees = Counter(x for x, _ in trust)
        in_degrees = Counter(y for _, y in trust)
        return next((i for i in range(1, n + 1) if in_degrees[i] == n - 1 and out_degrees[i] == 0), -1)

        # if n == 1:
        #     return 1
        # trust_others = set()
        # trusted_by_others = defaultdict(int)
        # judge = -1
        # maybe_judge = []
        # for p1, p2 in trust:
        #     trust_others.add(p1)
        #     trusted_by_others[p2] += 1
        #     if trusted_by_others[p2] == n - 1:
        #         maybe_judge.append(p2)
        # for j in maybe_judge:
        #     if j not in trust_others:
        #         if judge == -1:
        #             judge = j
        #         else:
        #             return -1
        # return judge


if __name__ == '__main__':
    s = Solution()
    print(s.findJudge(n=4, trust=[[1, 3], [1, 4], [2, 3], [2, 4], [4, 3]]))
