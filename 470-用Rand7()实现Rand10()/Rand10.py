# -*- coding: utf-8 -*-
# LeetCode 470-用Rand7()实现Rand10()

"""
Created on Sun Sept 5 22:58 2021

@author: _Mumu
Environment: py38
"""


# The rand7() API is already defined for you.
# def rand7():
# @return a random integer in the range 1 to 7
def rand7():
    from random import randint
    return randint(1, 7)


class Solution:
    def rand10(self):
        """
        :rtype: int
        """
        while True:
            row = rand7()
            col = rand7()
            idx = (row - 1) * 7 + col
            if idx <= 40:
                return idx % 10 + 1
            col = rand7()
            idx -= 40
            idx = (idx - 1) * 7 + col
            if idx <= 60:
                return idx % 10 + 1
            col = rand7()
            idx -= 20
            idx = (idx - 1) * 7 + col
            if idx <= 20:
                return idx % 10 + 1


if __name__ == '__main__':
    s = Solution()
    for i in range(50):
        print(s.rand10(), end=' ')
        if i % 10 == 9:
            print()
