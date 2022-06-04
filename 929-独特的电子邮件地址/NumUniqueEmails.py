# -*- coding: utf-8 -*-
# LeetCode 929-独特的电子邮件地址

"""
Created on Sat Jun 4 09:56 2022

@author: _Mumu
Environment: py38
"""

from collections import defaultdict
from typing import List


class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        addresses = defaultdict(set)
        for email in emails:
            name, site = email.split('@')
            addresses[site].add(name.split('+')[0].replace('.', ''))
        return sum(len(val) for val in addresses.values())


if __name__ == '__main__':
    s = Solution()
    print(s.numUniqueEmails(["a@leetcode.com", "b@leetcode.com", "c@leetcode.com"]))
