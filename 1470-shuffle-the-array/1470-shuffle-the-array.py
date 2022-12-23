class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        a=nums[:n]
        b=nums[n:]
        c=[]
        for i in range(len(a)):
            c.append(a[i])
            c.append(b[i])
        return c