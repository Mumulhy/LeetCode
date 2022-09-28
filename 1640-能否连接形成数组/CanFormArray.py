# -*- coding: utf-8 -*-
# LeetCode 1640-能否连接形成数组

"""
Created on Thu Sept 22 09:38 2022

@author: _Mumu
Environment: py39
"""

from typing import List


class Solution:
    def canFormArray(self, arr: List[int], pieces: List[List[int]]) -> bool:
        n = len(arr)
        pieces = {piece[0]: piece for piece in pieces}
        i = 0
        while i < n and arr[i] in pieces:
            piece = pieces[arr[i]]
            if arr[i:i + len(piece)] == piece:
                i += len(piece)
            else:
                return False
        return i == n


if __name__ == '__main__':
    s = Solution()
    print(s.canFormArray(arr=[91, 4, 64, 78], pieces=[[78], [4, 64], [91]]))
