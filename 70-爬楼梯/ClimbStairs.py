class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
        dp_i_2, dp_i_1 = 1, 1
        for _ in range(2, n + 1):
            dp_i = dp_i_2 + dp_i_1
            dp_i_2, dp_i_1 = dp_i_1, dp_i
        return dp_i
