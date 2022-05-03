# -*- coding: utf-8 -*-
# LeetCode 937-重新排列日志文件

"""
Created on Tues May 3 11:44 2022

@author: _Mumu
Environment: py38
"""

from typing import List


class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        number_log = []
        letter_log = []
        for log in logs:
            if log[-1].isdigit():
                number_log.append(log)
            else:
                log_split = log.split(' ')
                letter_log.append((log_split[1:], log_split[:1]))
        letter_log.sort()
        return [' '.join(log[1] + log[0]) for log in letter_log] + number_log


if __name__ == '__main__':
    s = Solution()
    print(s.reorderLogFiles(["dig1 8 1 5 1", "let1 art can", "dig2 3 6", "let2 own kit dig", "let3 art zero"]))
