# -*- coding: utf-8 -*-
# LeetCode 804-唯一摩尔斯密码词

"""
Created on Sun Apr 10 11:07 2022

@author: _Mumu
Environment: py38
"""

from typing import List


class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        morse = [".-", "-...", "-.-.", "-..", ".", "..-.", "--.", "....", "..", ".---", "-.-", ".-..", "--", "-.",
                 "---", ".--.", "--.-", ".-.", "...", "-", "..-", "...-", ".--", "-..-", "-.--", "--.."]
        reps = set()
        for word in words:
            rep = ''
            for letter in word:
                rep += morse[ord(letter) - ord('a')]
            reps.add(rep)
        return len(reps)


if __name__ == '__main__':
    s = Solution()
    print(s.uniqueMorseRepresentations(["gin", "zen", "gig", "msg"]))
