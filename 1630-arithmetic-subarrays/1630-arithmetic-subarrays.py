class Solution:
    def checkArithmeticSubarrays(self, nums: List[int], l: List[int], r: List[int]) -> List[bool]:
        res=[]
        for i, j in zip(l, r):
            s=True
            part=nums[i:j+1]
            part.sort()
            for i in range(len(part)-2):
                if part[i+2]-part[i+1] != part[i+1]-part[i]:
                    res.append(False)
                    s=False
                    break
            if s != False:
                res.append(True)            
        return res