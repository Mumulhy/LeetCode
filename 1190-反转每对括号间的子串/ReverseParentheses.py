# -*- coding: utf-8 -*-
# LeetCode 1190-反转每对括号间的子串

"""
Created on Fri May 26 23:30 2021

@author: _Mumu
Environment: py38
"""


class Solution:
    def reverseParentheses(self, s: str) -> str:
        s_reversed = [[]]
        for letter in s:
            if letter == '(':
                s_reversed.append([])
            elif letter == ')':
                now_layer = s_reversed.pop()
                s_reversed[-1] += now_layer[::-1]
            else:
                s_reversed[-1].append(letter)
        return ''.join(s_reversed[0])

        # s_reversed = []
        # for item in s:
        #     if item != ')':
        #         s_reversed.append(item)
        #     else:
        #         now_layer = []
        #         while s_reversed and s_reversed[-1] != '(':
        #             now_layer.append(s_reversed.pop())
        #         s_reversed.pop()
        #         s_reversed += now_layer
        # return ''.join(s_reversed)


if __name__ == '__main__':
    s = Solution()
    print(s.reverseParentheses("a(bcdefghijkl(mno)p)q"))
