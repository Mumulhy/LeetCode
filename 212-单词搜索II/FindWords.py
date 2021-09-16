# -*- coding: utf-8 -*-
# LeetCode 212-单词搜索II

"""
Created on Thu Sept 16 23:07 2021

@author: _Mumu
Environment: py38
"""

from collections import defaultdict
from typing import List


class Trie:
    def __init__(self):
        self.children = defaultdict(Trie)
        self.word = ''

    def insert(self, word: str) -> None:
        node = self
        for letter in word:
            node = node.children[letter]
        node.word = word


class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        m = len(board)
        n = len(board[0])
        wordsFound = []
        root = Trie()
        for word in words:
            root.insert(word)

        def search(node: Trie, i: int, j: int) -> None:
            if board[i][j] not in node.children:
                return

            letter = board[i][j]
            nodeNext = node.children[letter]
            if nodeNext.word:
                wordsFound.append(nodeNext.word)
                nodeNext.word = ''

            if nodeNext.children:
                board[i][j] = '#'
                for i1, j1 in [(i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)]:
                    if 0 <= i1 < m and 0 <= j1 < n:
                        search(nodeNext, i1, j1)
                board[i][j] = letter

            if not nodeNext.children:
                node.children.pop(letter)

        for a in range(m):
            for b in range(n):
                search(root, a, b)

        return wordsFound


if __name__ == '__main__':
    s = Solution()
    print(s.findWords(board=[["o", "a", "a", "n"],
                             ["e", "t", "a", "e"],
                             ["i", "h", "k", "r"],
                             ["i", "f", "l", "v"]],
                      words=["oath", "pea", "eat", "rain"]))
