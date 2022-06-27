# -*- coding: utf-8 -*-
# LeetCode 522-最长特殊序列II

"""
Created on Mon Jun 27 10:37 2022

@author: _Mumu
Environment: py38
"""

from typing import List


class Solution:
    def findLUSlength(self, strs: List[str]) -> int:
        def is_subseq(s: str, t: str) -> bool:
            ps = pt = 0
            ns, nt = len(s), len(t)
            while ps < ns and pt < nt:
                if s[ps] == t[pt]:
                    ps += 1
                pt += 1
            return ps == ns

        ans = -1
        for i, s in enumerate(strs):
            check = True
            for j, t in enumerate(strs):
                if i != j and is_subseq(s, t):
                    check = False
                    break
            if check:
                ans = max(ans, len(s))

        return ans


if __name__ == '__main__':
    s = Solution()
    print(s.findLUSlength(["aaa", "aaa", "aa"]))
