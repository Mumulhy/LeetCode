# -*- coding: utf-8 -*-
# LeetCode 1078-Bigram分词

"""
Created on Sun Dec 26 17:45 2021

@author: _Mumu
Environment: py38
"""

from typing import List


class Solution:
    def findOcurrences(self, text: str, first: str, second: str) -> List[str]:
        flag = -1
        ans = []
        for word in text.split(' '):
            if flag == 1:
                ans.append(word)
                if first == second:
                    flag = 0
                else:
                    flag = -1
            if word == second and flag == 0:
                flag = 1
            elif word == first:
                flag = 0
            else:
                flag = -1
        return ans
