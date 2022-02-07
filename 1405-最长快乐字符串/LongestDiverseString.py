# -*- coding: utf-8 -*-
# LeetCode 1405-最长快乐字符串

"""
Created on Mon Feb 7 20:39 2022

@author: _Mumu
Environment: py38
"""


class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        if a == b == c == 0:
            return ''
        ans = ''
        letters_left = []
        if a > 0:
            letters_left.append([a, 'a'])
        if b > 0:
            letters_left.append([b, 'b'])
        if c > 0:
            letters_left.append([c, 'c'])
        letters_left.sort(reverse=True)
        while len(letters_left) > 1:
            if ans and ans[-1] == letters_left[0][1]:
                if letters_left[0][0] >= letters_left[1][0] * 2 - 2:
                    ans += letters_left[1][1]
                    letters_left[1][0] -= 1
                else:
                    k = min(letters_left[1][0], 2)
                    ans += letters_left[1][1] * k
                    letters_left[1][0] -= k
                if letters_left[1][0] == 0:
                    letters_left.pop(1)
            else:
                k = min(letters_left[0][0], 2)
                ans += letters_left[0][1] * k
                letters_left[0][0] -= k
                if letters_left[0][0] == 0:
                    letters_left.pop(0)
            letters_left.sort(reverse=True)
        if letters_left:
            k = min(letters_left[0][0], 2)
            ans += letters_left[0][1] * k
        return ans


if __name__ == '__main__':
    s = Solution()
    print(s.longestDiverseString(a=0, b=8, c=11))
