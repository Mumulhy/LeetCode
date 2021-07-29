# -*- coding: utf-8 -*-
# LeetCode 1104-二叉树寻路

"""
Created on Thu Jul 29 18:01 2021

@author: _Mumu
Environment: py38
"""

from typing import List


class Solution:
    def pathInZigZagTree(self, label: int) -> List[int]:
        self.bin = bin(label)[2:]
        self.bin_r = '1' + ''.join(['0' if j == '1' else '1' for j in self.bin[1:]])
        self.bin_len_mod_2 = len(self.bin) % 2
        self.path = []
        for i in range(len(self.bin)):
            if i % 2 == self.bin_len_mod_2:
                self.path.append(int(self.bin_r[:i + 1], 2))
            else:
                self.path.append(int(self.bin[:i + 1], 2))
        return self.path


if __name__ == '__main__':
    s = Solution()
    print(s.pathInZigZagTree(5))
