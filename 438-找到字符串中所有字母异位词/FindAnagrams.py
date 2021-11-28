# -*- coding: utf-8 -*-
# LeetCode 438-找到字符串中所有字母异位词

"""
Created on Sun Nov 28 13:50 2021

@author: _Mumu
Environment: py38
"""

# from collections import defaultdict
from typing import List


class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        n = len(p)
        m = len(s)
        if m < n:
            return []
        cnt = [0] * 26
        for i in range(n):
            cnt[ord(s[i]) - 97] += 1
            cnt[ord(p[i]) - 97] -= 1
        differ = [c != 0 for c in cnt].count(True)
        ans = []
        if differ == 0:
            ans.append(0)
        for i in range(m - n):
            cnt[ord(s[i]) - 97] -= 1
            if cnt[ord(s[i]) - 97] == 0:
                differ -= 1
            elif cnt[ord(s[i]) - 97] == -1:
                differ += 1
            cnt[ord(s[i + n]) - 97] += 1
            if cnt[ord(s[i + n]) - 97] == 0:
                differ -= 1
            elif cnt[ord(s[i + n]) - 97] == 1:
                differ += 1
            if differ == 0:
                ans.append(i + 1)
        return ans

        # n = len(p)
        # cnt = defaultdict(int)
        # for letter in p:
        #     cnt[letter] += 1
        # curr_cnt = defaultdict(int)
        # for letter in s[:n]:
        #     curr_cnt[letter] += 1
        # ans = []
        # if curr_cnt == cnt:
        #     ans.append(0)
        # for i in range(len(s) - n):
        #     if s[i] == s[i + n]:
        #         if ans and i == ans[-1]:
        #             ans.append(i + 1)
        #     else:
        #         if curr_cnt[s[i]] == 1:
        #             curr_cnt.pop(s[i])
        #         else:
        #             curr_cnt[s[i]] -= 1
        #         curr_cnt[s[i + n]] += 1
        #         if curr_cnt == cnt:
        #             ans.append(i + 1)
        # return ans


if __name__ == '__main__':
    s = Solution()
    print(s.findAnagrams(s="aabaa", p="ab"))
