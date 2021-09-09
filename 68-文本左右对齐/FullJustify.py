# -*- coding: utf-8 -*-
# LeetCode 68-文本左右对齐

"""
Created on Thur Sept 9 15:18 2021

@author: _Mumu
Environment: py38
"""

from typing import List


class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        left, right = 0, 1
        n = len(words)
        nowLen = len(words[0])
        linesJustified = []
        while right < n:
            nowLen += 1 + len(words[right])
            if nowLen > maxWidth:
                newLine = ''
                nowLen -= 1 + len(words[right])
                gaps = right - 1 - left
                spaces = maxWidth - nowLen + gaps
                if gaps == 0:
                    newLine = words[left] + ' ' * spaces
                else:
                    mod = spaces % gaps
                    for word in words[left:right - 1]:
                        newLine += word + ' ' * (spaces // gaps)
                        if mod:
                            newLine += ' '
                            mod -= 1
                    newLine += words[right - 1]
                linesJustified.append(newLine)
                nowLen = len(words[right])
                left = right
            right += 1
        linesJustified.append(' '.join(words[left:]) + ' ' * (maxWidth - nowLen))
        return linesJustified


if __name__ == '__main__':
    s = Solution()
    for line in s.fullJustify(words=["Science", "is", "what", "we", "understand", "well", "enough", "to", "explain",
                                     "to", "a", "computer.", "Art", "is", "everything", "else", "we", "do"],
                              maxWidth=20):
        print(line)
