# -*- coding: utf-8 -*-
# LeetCode 208-实现Trie(前缀树)

"""
Created on Thu Sept 16 22:11 2021

@author: _Mumu
Environment: py38
"""


class Trie:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.children = [0] * 26
        self.isEnd = False

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        node = self
        for letter in word:
            letter_id = ord(letter) - 97
            if not node.children[letter_id]:
                node.children[letter_id] = Trie()
            node = node.children[letter_id]
        node.isEnd = True

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        node = self
        for letter in word:
            letter_id = ord(letter) - 97
            if node.children[letter_id]:
                node = node.children[letter_id]
            else:
                return False
        return node.isEnd

    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        node = self
        for letter in prefix:
            letter_id = ord(letter) - 97
            if node.children[letter_id]:
                node = node.children[letter_id]
            else:
                return False
        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)

if __name__ == '__main__':
    root = Trie()
    root.insert('word')
    print(root.search('word'))
    root.insert('wor')
    print(root.search('wor'))
    print(root.search('word'))
    print(root.search('world'))
    print(root.startsWith('worl'))
