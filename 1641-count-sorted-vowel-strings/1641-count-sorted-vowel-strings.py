class Solution:
    def countVowelStrings(self, n: int) -> int:
        # dp[i][j]: number of strings of length i that end with vowel j
        dp = [[0] * 5 for _ in range(n+1)]

        # Base case: For length 1, there's 1 string per vowel
        for j in range(5):
            dp[1][j] = 1

        # Fill in the DP table
        for i in range(2, n+1):  # For each length from 2 to n
            for j in range(5):  # For each vowel
                # Sum of all strings of length i-1 that end with a vowel <= j
                dp[i][j] = sum(dp[i-1][k] for k in range(j+1))

        # The answer is the sum of strings of length n ending with any vowel
        return sum(dp[n])