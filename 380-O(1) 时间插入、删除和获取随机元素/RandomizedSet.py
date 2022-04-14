# -*- coding: utf-8 -*-
# LeetCode 380-O(1) 时间插入、删除和获取随机元素

"""
Created on Wed Apr 13 11:43 2022

@author: _Mumu
Environment: py38
"""

from random import choice


class RandomizedSet:
    def __init__(self):
        self.list = []
        self.dict = {}
        self.len = 0

    def insert(self, val: int) -> bool:
        if val in self.dict:
            return False
        self.list.append(val)
        self.dict[val] = self.len
        self.len += 1
        return True

    def remove(self, val: int) -> bool:
        if val not in self.dict:
            return False
        self.len -= 1
        self.list[self.dict[val]] = self.list[self.len]
        self.dict[self.list[self.len]] = self.dict[val]
        self.list.pop()
        self.dict.pop(val)
        return True

    def getRandom(self) -> int:
        return choice(self.list)

# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
