# -*- coding: utf-8 -*-
# LeetCode 648-单词替换

"""
Created on Thu Jul 7 11:07 2022

@author: _Mumu
Environment: py38
"""

from typing import List


class Trie:
    def __init__(self):
        self.is_end = False
        self.children = [None] * 26

    def insert(self, word: str) -> None:
        node = self
        for letter in word:
            if node.is_end:
                return
            idx = ord(letter) - ord('a')
            if not node.children[idx]:
                node.children[idx] = Trie()
            node = node.children[idx]
        node.is_end = True
        return

    def find(self, word: str) -> int:
        node = self
        k = 0
        for letter in word:
            idx = ord(letter) - ord('a')
            if node.is_end or not node.children[idx]:
                break
            node = node.children[idx]
            k += 1
        return k if node.is_end else 0


class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        trie = Trie()
        for word in dictionary:
            trie.insert(word)
        spl = sentence.split(' ')
        for i in range(len(spl)):
            k = trie.find(spl[i])
            if k:
                spl[i] = spl[i][:k]
        return ' '.join(spl)


if __name__ == '__main__':
    s = Solution()
    print(s.replaceWords(dictionary=["cat", "bat", "rat"], sentence="the cattle was rattled by the battery rat"))
