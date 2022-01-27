# -*- coding: utf-8 -*-
# LeetCode 2047-句子中的有效单词数

"""
Created on Thu Jan 27 19:49 2022

@author: _Mumu
Environment: py38
"""


class Solution:
    def countValidWords(self, sentence: str) -> int:
        ans = 0
        for word in sentence.split(' '):
            if word:
                last_ch = '#'
                is_word = True
                is_join = False
                for ch in word:
                    if '0' <= ch <= '9' or last_ch in '!.,' or (ch == '-' and last_ch == '#'):
                        is_word = False
                        break
                    if ch == '-':
                        if is_join:
                            is_word = False
                            break
                        is_join = True
                    if last_ch == '-' and ch in '!.,':
                        is_word = False
                        break
                    last_ch = ch
                if last_ch == '-':
                    is_word = False
                if is_word:
                    ans += 1
        return ans


if __name__ == '__main__':
    s = Solution()
    print(s.countValidWords('asd'))
