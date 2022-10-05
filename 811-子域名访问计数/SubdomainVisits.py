# -*- coding: utf-8 -*-
# LeetCode 811-子域名访问计数

"""
Created on Wed Oct 5 10:52 2022

@author: _Mumu
Environment: py38
"""

from collections import defaultdict
from typing import List


class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        cnt = defaultdict(int)
        for cpdomain in cpdomains:
            num, domain = cpdomain.split()
            num = int(num)
            domains = domain.split('.')
            n = len(domains)
            for i in range(n):
                cnt['.'.join(domains[i:n])] += num
        return [f'{val} {key}' for key, val in cnt.items()]


if __name__ == '__main__':
    s = Solution()
    print(s.subdomainVisits(["900 google.mail.com", "50 yahoo.com", "1 intel.mail.com", "5 wiki.org"]))
