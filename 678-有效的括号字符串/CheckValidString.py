# -*- coding: utf-8 -*-
# LeetCode 678-有效的括号字符串

"""
Created on Sun Sept 12 19:02 2021

@author: _Mumu
Environment: py38
"""


class Solution:
    def checkValidString(self, s: str) -> bool:
        inf = sup = 0
        for item in s:
            if item == '(':
                inf += 1
                sup += 1
            elif item == ')':
                inf = max(inf - 1, 0)
                sup -= 1
                if sup < 0:
                    return False
            else:
                inf = max(inf - 1, 0)
                sup += 1
        return inf == 0

        # lefts = []
        # stars = []
        # for i in range(len(s)):
        #     if s[i] == '(':
        #         lefts.append(i)
        #     elif s[i] == '*':
        #         stars.append(i)
        #     else:
        #         if lefts:
        #             lefts.pop(-1)
        #         elif stars:
        #             stars.pop(-1)
        #         else:
        #             return False
        # while lefts and stars:
        #     if lefts[-1] < stars[-1]:
        #         lefts.pop(-1)
        #         stars.pop(-1)
        #     else:
        #         return False
        # return False if lefts else True


if __name__ == '__main__':
    s = Solution()
    print(s.checkValidString('(*))'))
