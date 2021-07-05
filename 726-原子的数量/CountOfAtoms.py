# -*- coding: utf-8 -*-
# LeetCode 726-原子的数量

"""
Created on Fri Jul 5 22:54 2021

@author: _Mumu
Environment: py38
"""


class Solution:
    def countOfAtoms(self, formula: str) -> str:
        formula_list = []
        atom = ''
        number = 0
        for i, item in enumerate(formula):
            if item == '(':
                if atom:
                    formula_list.append(atom)
                    if number:
                        formula_list.append(number)
                    else:
                        formula_list.append(1)
                formula_list.append(item)
                atom = ''
                number = 0
            elif ord('A') <= ord(item) <= ord('Z') or item == ')':
                if atom:
                    formula_list.append(atom)
                    if number:
                        formula_list.append(number)
                    else:
                        formula_list.append(1)
                atom = item
                number = 0
            elif ord('a') <= ord(item) <= ord('z'):
                atom += item
            else:
                number = number * 10 + int(item)
        if atom:
            formula_list.append(atom)
            if number:
                formula_list.append(number)
            else:
                formula_list.append(1)
        # print(formula_list)
        k = 0
        for item in formula_list:
            if item == '(':
                k += 1
        left_index = 0
        right_index = 0
        for _ in range(k):
            for i, item in enumerate(formula_list):
                if item == ')':
                    right_index = i
                    for j in range(i, -1, -1):
                        if formula_list[j] == '(':
                            left_index = j
                            break
                    for j in range(left_index, right_index):
                        if isinstance(formula_list[j], int):
                            formula_list[j] = formula_list[j] * formula_list[right_index + 1]
                    formula_list.pop(right_index + 1)
                    formula_list.pop(right_index)
                    formula_list.pop(left_index)
                    break
        # print(formula_list)
        count_atoms = {}
        for i in range(len(formula_list)):
            if isinstance(formula_list[i], int):
                if formula_list[i - 1] in count_atoms:
                    count_atoms[formula_list[i - 1]] += formula_list[i]
                else:
                    count_atoms[formula_list[i - 1]] = formula_list[i]
        # print(count_atoms)
        result = ''
        for item in sorted(count_atoms):
            result += item
            if count_atoms[item] != 1:
                result += str(count_atoms[item])
        return result


if __name__ == '__main__':
    s = Solution()
    print(s.countOfAtoms('H12KAl(S(OH)6O4)2'))
