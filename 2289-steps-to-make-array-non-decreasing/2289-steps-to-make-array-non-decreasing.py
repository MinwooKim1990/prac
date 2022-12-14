import numpy as np
class Solution:
    def totalSteps(self, nums: List[int]) -> int:
        ans = 0
        nums.reverse()
        list = [[nums[0], 0]]
        for i in range(1, len(nums)):
            count = 0
            while list and list[-1][0] < nums[i]:
                count = max(count + 1, list[-1][1])
                list.pop()
            list.append([nums[i], count])
            ans = max(ans, count)
        return ans