import numpy as np

class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        # There's no need for np.nan and a separate 'cal' function; we can compute directly.
        # Initialize the DP table directly with the values from the triangle for the first row and inf for others.
        n = len(triangle)
        dp = [float('inf')] * n
        dp[0] = triangle[0][0]

        # Iterate through the triangle, updating the DP table in-place.
        for i in range(1, n):
            # Iterate from the end to start to avoid overwriting values we still need.
            for j in range(i, -1, -1):
                if j == 0:  # First element of each row
                    dp[j] = dp[j] + triangle[i][j]
                elif j == i:  # Last element of each row (i == j)
                    dp[j] = dp[j-1] + triangle[i][j]
                else:  # Middle elements
                    dp[j] = min(dp[j], dp[j-1]) + triangle[i][j]

        # The minimum path sum is the minimum value in the last row of the DP table.
        return min(dp)
