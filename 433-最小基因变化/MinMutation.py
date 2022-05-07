# -*- coding: utf-8 -*-
# LeetCode 433-最小基因变化

"""
Created on Sat May 7 11:47 2022

@author: _Mumu
Environment: py38
"""

from typing import List


class Solution:
    def minMutation(self, start: str, end: str, bank: List[str]) -> int:
        stack = {start}
        visited = {start}
        ans = 0
        while stack:
            for gene in stack:
                if gene == end:
                    return ans
            new_stack = set()
            for gene in stack:
                for x in bank:
                    if x in visited:
                        continue
                    cnt = 0
                    for i in range(8):
                        if gene[i] != x[i]:
                            if cnt == 1:
                                cnt = 0
                                break
                            cnt = 1
                    if cnt:
                        new_stack.add(x)
            stack = new_stack
            visited |= stack
            ans += 1
        return -1


if __name__ == '__main__':
    s = Solution()
    print(s.minMutation(start="AAAAACCC", end="AACCCCCC", bank=["AAAACCCC", "AACCCCCC"]))
