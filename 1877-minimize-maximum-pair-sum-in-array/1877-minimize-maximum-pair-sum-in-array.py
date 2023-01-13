import numpy as np
class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        print(sorted(nums)[::-1])
        print(sorted(nums))
        return max(a + b for a, b in zip(sorted(nums), sorted(nums)[::-1]))