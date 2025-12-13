# -*- coding: utf-8 -*-
# LeetCode 3606-优惠券校验器

"""
Created on Sat Dec 13 20:12 2025

@author: _Mumu
Environment: py38
"""

from typing import List


class Solution:
    def validateCoupons(self, code: List[str], businessLine: List[str], isActive: List[bool]) -> List[str]:
        def is_valid_id(cp_id: str):
            for char in cp_id:
                if not (char == '_' or char.isdigit() or char.islower() or char.isupper()):
                    return False
            return cp_id is not ''

        valid_ids = []
        biz_map = {"electronics": 0, "grocery": 1, "pharmacy": 2, "restaurant": 3}
        for coupon_id, biz, is_valid_cp in zip(code, businessLine, isActive):
            if is_valid_cp and biz in biz_map and is_valid_id(coupon_id):
                valid_ids.append((coupon_id, biz))
        valid_ids.sort(key=lambda x: (biz_map[x[1]], x[0]))
        return [coupon_id for coupon_id, _ in valid_ids]
