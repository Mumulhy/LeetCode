# -*- coding: utf-8 -*-
# LeetCode 707-设计链表

"""
Created on Wed Oct 2 00:07 2019

@author: _Mumu
Environment: py37
"""

class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:

        flag = 1                                 # 标记是否有需要删除的部分
        current_len = 1                          # 标记当前连续相同字符个数
        while flag == 1:                         # 若无需要删除的部分跳出循环
            List = []                            # 使用列表作为栈
            flag = 0
            x0 = 0                               # 存储前一个字符
            for x in s:
                List.append(x)                   # 入栈
                if x == x0:                      # 与前一个字符相同则当前连续相同字符数+1
                    current_len += 1
                else:                            # 不同则数目重新置1，并将x0置0
                    current_len = 1
                    x0 = x
                if current_len == k:             # 当前连续相同字符数达到k
                    i = 1
                    while i <= k:                # 作k次出栈操作
                        List.pop(len(List)-1)
                        i += 1
                    flag = 1                     # 删除过元素，标记置1
                    current_len = 1
                    x0 = 0
            s = ""
            for x in List:                       # 存储操作后的字符串，用于下次循环或输出
                s += x
        return s

        # 以下为本题运行最快的算法

        # f =True
        # while f:
        #     f=False
        #     d = 'abcdefghijklmnopqrstuvwxyz'
        #     for i in d:
        #         while i * k in s:
        #             s = s.replace(i * k, '')
        #             f = True
        # return s