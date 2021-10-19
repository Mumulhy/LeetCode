# -*- coding: utf-8 -*-
# LeetCode 211-添加与搜索单词-数据结构设计

"""
Created on Tues Oct 19 22:33 2021

@author: _Mumu
Environment: py38
"""

from collections import defaultdict
# from typing import List

class WordDictionary:
    def __init__(self):
        self.dic = defaultdict(list)

    def addWord(self, word: str) -> None:
        n = len(word)
        self.dic[n].append(word)
        return

    def search(self, word: str) -> bool:
        n = len(word)
        if n not in self.dic:
            return False
        if word in self.dic[n]:
            return True
        for w in self.dic[n]:
            i = 0
            while i < n:
                if word[i] == '.' or word[i] == w[i]:
                    i += 1
                    if i == n:
                        return True
                else:
                    break
        return False


# class WordDictionary:
#     def __init__(self):
#         self.nextLetter = [None] * 26
#         self.isWord = False
#
#     def addWord(self, word: str) -> None:
#         node = self
#         for letter in word:
#             idx = ord(letter) - ord('a')
#             if not node.nextLetter[idx]:
#                 node.nextLetter[idx] = WordDictionary()
#             node = node.nextLetter[idx]
#         node.isWord = True
#         return
#
#     def search(self, word: str) -> bool:
#         n = len(word) - 1
#         stack: List[(WordDictionary, int)] = []
#         if word[0] == '.':
#             for nextLetter in self.nextLetter:
#                 if nextLetter:
#                     stack.append((nextLetter, 0))
#         else:
#             idx = ord(word[0]) - ord('a')
#             if self.nextLetter[idx]:
#                 stack.append((self.nextLetter[idx], 0))
#         while stack:
#             node, i = stack.pop()
#             if i == n:
#                 if node.isWord:
#                     return True
#                 continue
#             i += 1
#             if word[i] == '.':
#                 for nextLetter in node.nextLetter:
#                     if nextLetter:
#                         stack.append((nextLetter, i))
#             else:
#                 idx = ord(word[i]) - ord('a')
#                 if node.nextLetter[idx]:
#                     stack.append((node.nextLetter[idx], i))
#         return False


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)

if __name__ == '__main__':
    dic = WordDictionary()
    dic.addWord('apple')
    dic.addWord('app')
    dic.addWord('apec')
    print(dic.search('.p..e'))
