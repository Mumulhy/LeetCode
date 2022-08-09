# -*- coding: utf-8 -*-
# LeetCode 761-特殊的二进制序列

"""
Created on Mon Aug 8 09:41 2022

@author: _Mumu
Environment: py39
"""

class Solution:
    def makeLargestSpecial(self, s: str) -> str:
        if len(s) <= 2:
            return s
        cnt = left = 0
        subs = []
        for i, ch in enumerate(s):
            if ch == '1':
                cnt += 1
            else:
                cnt -= 1
                if cnt == 0:
                    subs.append('1' + self.makeLargestSpecial(s[left + 1:i]) + '0')
                    left = i + 1
        subs.sort(reverse=True)
        return ''.join(subs)

if __name__ == '__main__':
    s = Solution()
    print(s.makeLargestSpecial("11011000"))