# -*- coding: utf-8 -*-
# LeetCode 1576-替换所有的问号

"""
Created on Wed Jan 5 10:24 2022

@author: _Mumu
Environment: py38
"""


class Solution:
    def modifyString(self, s: str) -> str:
        n = len(s)
        last_ch = ''
        res = ''
        for i in range(n):
            if s[i] == '?':
                if i == n - 1:
                    next_ch = ''
                else:
                    next_ch = s[i + 1]
                modified_ch = ''
                for ch in 'abc':
                    if ch != last_ch and ch != next_ch:
                        modified_ch = ch
                        break
                res += modified_ch
                last_ch = modified_ch
            else:
                res += s[i]
                last_ch = s[i]
        return res


if __name__ == '__main__':
    s = Solution()
    print(s.modifyString("a????c????b??????c?a?"))
