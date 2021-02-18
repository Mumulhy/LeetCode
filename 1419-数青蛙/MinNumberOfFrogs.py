# -*- coding: utf-8 -*-
# LeetCode 1419-数青蛙

"""
Created on Thu Feb 18 16:37 2021

@author: _Mumu
Environment: py37
"""

class Solution:
    def minNumberOfFrogs(self, croakOfFrogs: str) -> int:
        croak = 'croak'
        croak_idt = {'c': 0, 'r': 1, 'o': 2, 'a': 3, 'k': 4}
        croak_num = {'c': 0, 'r': 0, 'o': 0, 'a': 0, 'k': 0}
        for letter in croakOfFrogs:
            if letter not in croak:
                return -1
            if letter == 'c':
                if croak_num['k'] == 0:
                    croak_num['c'] += 1
                else:
                    croak_num['k'] -= 1
                    croak_num['c'] += 1
            else:
                if croak_num[croak[croak_idt[letter]-1]] == 0:
                    return -1
                else:
                    croak_num[croak[croak_idt[letter]-1]] -= 1
                    croak_num[croak[croak_idt[letter]]] += 1
        if croak_num['c'] + croak_num['r'] + croak_num['o'] + croak_num['a'] == 0:
            return croak_num['k']
        else:
            return -1

        # 以下是自己写的时间复杂度为O(n^2)的代码

        # croak = 'croak'
        # croak_id = {'c': 0, 'r': 1, 'o': 2, 'a': 3, 'k': 4}
        # frogs = []
        # for letter in croakOfFrogs:
        #     if letter in croak:
        #         if letter == 'c':
        #             if frogs:
        #                 done = 0
        #                 for i, frog in enumerate(frogs):
        #                     if frog[-1] == 'k':
        #                         frogs[i] += letter
        #                         done = 1
        #                         break
        #                 if not done:
        #                     frogs.append(letter)
        #             else:
        #                 frogs.append(letter)
        #         else:
        #             done = 0
        #             for i, frog in enumerate(frogs):
        #                 if frog[-1] == croak[croak_id[letter]-1]:
        #                     frogs[i] += letter
        #                     done = 1
        #                     break
        #             if not done:
        #                 return -1
        #     else:
        #         return -1
        #     print(frogs)
        # for frog in frogs:
        #     if frog[-1] != 'k':
        #         return -1
        # return len(frogs)

if __name__ == '__main__':
    s = Solution()
    print(s.minNumberOfFrogs('crocarkoacroakk'))