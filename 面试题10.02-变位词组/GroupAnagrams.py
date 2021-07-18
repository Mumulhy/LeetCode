# -*- coding: utf-8 -*-
# LeetCode 面试题10.02-变位词组

"""
Created on Sun Jul 18 17:30 2021

@author: _Mumu
Environment: py38
"""

from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        sorted_strs = {}
        for string in strs:
            sorted_string = ''.join(sorted(string))
            if sorted_string in sorted_strs:
                sorted_strs[sorted_string].append(string)
            else:
                sorted_strs[sorted_string] = [string]
        return list(sorted_strs.values())

        # 自己写的暴力计数的代码，执行用时和内存消耗都只有5%
        # dicts = []
        # groups = []
        # for string in strs:
        #     now_dict = {}
        #     for letter in string:
        #         if letter in now_dict:
        #             now_dict[letter] += 1
        #         else:
        #             now_dict[letter] = 1
        #     if now_dict in dicts:
        #         groups[dicts.index(now_dict)].append(string)
        #     else:
        #         dicts.append(now_dict)
        #         groups.append([string])
        # return groups


if __name__ == '__main__':
    s = Solution()
    print(s.groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))
