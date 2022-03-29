# -*- coding: utf-8 -*-
# LeetCode 2024-考试的最大困扰度

"""
Created on Tues Mar 29 10:34 2022

@author: _Mumu
Environment: py38
"""


class Solution:
    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:
        def max_consecutive_char(ch: str) -> int:
            ans, left, num = 0, 0, 0
            for right in range(len(answerKey)):
                num += answerKey[right] != ch
                while num > k:
                    num -= answerKey[left] != ch
                    left += 1
                ans = max(ans, right - left + 1)
            return ans
        return max(max_consecutive_char('T'), max_consecutive_char('F'))

        # left = 0
        # right = 0
        # ans = 0
        # n = len(answerKey)
        # cnt = {'T': 0, 'F': 0}
        # while True:
        #     while min(cnt.values()) <= k and right < n:
        #         cnt[answerKey[right]] += 1
        #         right += 1
        #     if min(cnt.values()) <= k:
        #         ans = max(ans, right - left)
        #     else:
        #         ans = max(ans, right - left - 1)
        #     if right == n:
        #         return ans
        #     while min(cnt.values()) > k:
        #         cnt[answerKey[left]] -= 1
        #         left += 1


if __name__ == '__main__':
    s = Solution()
    print(s.maxConsecutiveAnswers(answerKey="TFFT", k=1))
