class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        # Initialize a DP list where each element is a list.
        # dp[i] will hold all unique combinations of numbers that sum up to 'i'.
        # Initially, every element is set to an empty list, indicating no combination found yet.
        dp = [[] for _ in range(target + 1)]
        
        # Populate the DP list
        # Start by considering each candidate number 'c' from the list of candidates.
        for c in candidates:
            # For each candidate, iterate through all sum values from 'c' to 'target'.
            # This helps in building combinations incrementally for each sum value.
            for sum_value in range(c, target + 1):
                # If the sum value matches the candidate,
                # it means the candidate itself forms a valid combination.
                # Therefore, initialize dp[sum_value] with a list containing just 'c'.
                if sum_value == c:
                    dp[sum_value].append([c])
                else:
                    # For sum values greater than 'c',
                    # look for combinations that sum up to 'sum_value - c'.
                    # These are combinations to which adding 'c' will form a new combination
                    # that sums up to 'sum_value'.
                    for combination in dp[sum_value - c]:
                        # Append 'c' to each such combination and add the new combination
                        # to the list of combinations for 'sum_value'.
                        dp[sum_value].append(combination + [c])

        # Return the list of combinations that sum up to the target.
        # This is the last element in the DP list, dp[target].
        return dp[target]
