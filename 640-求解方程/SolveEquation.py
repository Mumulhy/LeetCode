# -*- coding: utf-8 -*-
# LeetCode 640-求解方程

"""
Created on Wed Aug 10 09:36 2022

@author: _Mumu
Environment: py39
"""


class Solution:
    def solveEquation(self, equation: str) -> str:
        xs = 0
        const = 0
        curr_state = 1
        curr_digit = 0
        is_plus = 1
        is_digit = False
        for ch in equation:
            if ch == 'x':
                if is_digit:
                    xs += curr_state * is_plus * curr_digit
                    curr_digit, is_digit = 0, False
                else:
                    xs += curr_state * is_plus
            elif ch in '+-=':
                if is_digit:
                    const -= curr_state * is_plus * curr_digit
                    curr_digit, is_digit = 0, False
                is_plus = 1 if ch in '+=' else -1
                if ch == '=':
                    curr_state = -1
            else:
                curr_digit = curr_digit * 10 + int(ch)
                is_digit = True
            print(ch, xs, const, curr_digit, curr_state, is_plus)
        if is_digit:
            const -= curr_state * is_plus * curr_digit
            print('end', xs, const, curr_digit)
        if xs == 0:
            return 'Infinite solutions' if const == 0 else 'No solution'
        return f'x={const // xs}'


if __name__ == '__main__':
    s = Solution()
    print(s.solveEquation("0x=0"))
