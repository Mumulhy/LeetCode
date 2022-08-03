# -*- coding: utf-8 -*-
# LeetCode 899-有序队列

"""
Created on Wed Aug 3 09:07 2022

@author: _Mumu
Environment: py38
"""


class Solution:
    def orderlyQueue(self, s: str, k: int) -> str:
        if k > 1:
            return ''.join(sorted(s))
        n = len(s)
        i, j, l = 0, 1, 0
        while j + l < n:
            if s[i + l] == s[j + l]:
                l += 1
                continue
            elif s[i + l] > s[j + l]:
                i += l + 1
            else:
                j += l + 1
            if i == j:
                j += 1
            l = 0
        return min(s[i:] + s[:i], s[j:] + s[:j])

        # ans = s
        # n = len(s)
        # for _ in range(n - 1):
        #     s = s[1:] + s[0]
        #     if s < ans:
        #         ans = s
        # return ans


if __name__ == '__main__':
    s = Solution()
    print(s.orderlyQueue(s="dabeab", k=1))
