class Solution:
    def tribonacci(self, n: int) -> int:
        # Base cases directly handled by DP table initialization
        if n == 0:
            return 0
        elif n == 1 or n == 2:
            return 1

        # Initialize DP table with base values
        dp = [0, 1, 1] + [0] * (n - 2)  # Pre-fill the list for n > 2

        # Fill DP table iteratively for n > 2
        for i in range(3, n + 1):
            dp[i] = dp[i - 1] + dp[i - 2] + dp[i - 3]

        # The nth Tribonacci number is stored at dp[n]
        return dp[n]
