# -*- coding: utf-8 -*-
# LeetCode 824-山羊拉丁文

"""
Created on Thu Apr 21 11:30 2022

@author: _Mumu
Environment: py38
"""


class Solution:
    def toGoatLatin(self, sentence: str) -> str:
        words = sentence.split(' ')
        aeiou = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}
        for i, word in enumerate(words):
            if word[0] in aeiou:
                words[i] = word + 'm' + 'a' * (i + 2)
            else:
                words[i] = word[1:] + word[0] + 'm' + 'a' * (i + 2)
        return ' '.join(words)


if __name__ == '__main__':
    s = Solution()
    print(s.toGoatLatin("I speak Goat Latin"))
