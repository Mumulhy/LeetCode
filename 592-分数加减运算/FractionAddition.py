# -*- coding: utf-8 -*-
# LeetCode 592-分数加减运算

"""
Created on Wed Jul 27 10:11 2022

@author: _Mumu
Environment: py38
"""


def GCD(a: int, b: int) -> int:
    a, b = max(a, b), min(a, b)
    t = a % b
    while t != 0:
        a, b = b, t
        t = a % b
    return b


def LCM(a: int, b: int) -> int:
    gcd = GCD(a, b)
    return a * b // gcd


class Solution:
    def fractionAddition(self, expression: str) -> str:
        expr = []
        curr = ''
        for ch in expression:
            if ch == '+':
                expr.append(list(map(int, curr.split('/'))))
                curr = ''
            elif ch == '-':
                if curr:
                    expr.append(list(map(int, curr.split('/'))))
                curr = '-'
            else:
                curr += ch
        expr.append(list(map(int, curr.split('/'))))
        if len(expr) == 1:
            return expression
        lcm = LCM(expr[0][1], expr[1][1])
        for f1, f2 in expr[2:]:
            lcm = LCM(lcm, f2)
        f1_sum = sum(f1 * lcm // f2 for f1, f2 in expr)
        if f1_sum == 0:
            return '0/1'
        gcd = GCD(abs(f1_sum), lcm)
        return str(f1_sum // gcd) + '/' + str(lcm // gcd)


if __name__ == '__main__':
    s = Solution()
    print(s.fractionAddition("-1/2+1/2+1/3"))
