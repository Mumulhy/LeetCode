# -*- coding: utf-8 -*-
# LeetCode 917-仅仅反转字母

"""
Created on Wed Feb 23 12:52 2022

@author: _Mumu
Environment: py38
"""


class Solution:
    def reverseOnlyLetters(self, s: str) -> str:
        n = len(s)
        p1, p2 = 0, n
        ans = []
        while p1 < n:
            if 65 <= ord(s[p1]) <= 90 or 97 <= ord(s[p1]) <= 122:
                p2 -= 1
                while not (65 <= ord(s[p2]) <= 90 or 97 <= ord(s[p2]) <= 122):
                    p2 -= 1
                ans.append(s[p2])
            else:
                ans.append(s[p1])
            p1 += 1
        return ''.join(ans)


if __name__ == '__main__':
    s = Solution()
    print(s.reverseOnlyLetters("Test1ng-Leet=code-Q!"))
