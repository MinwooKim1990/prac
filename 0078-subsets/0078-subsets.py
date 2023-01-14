import math
import itertools
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
#        res=[]
#        for r in range(len(nums)):
#            for i in #range(math.factorial(len(nums))/(math.factorial(r+1)*math.factorial(len(nums)-#(r+1)))):
#                temp=[nums[i]]
#                res.append(temp)
        res=[]
        for x in range(len(set(nums))+1):
            res+=list(combinations(set(nums), x))
        return res