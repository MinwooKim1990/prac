from collections import Counter
class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        a = dict(Counter(nums))
        res=0
        alist=[i for i in a.values()]
        for i in range(len(alist)):
            res+=alist[i]*(alist[i]-1)/2
        return int(res)