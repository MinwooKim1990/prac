import numpy as np
class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        if len(nums)<3:
            if nums !=[]:
                return np.max(nums)
        else:
            max={}
            for i in range(3):
                temp=[]
                if nums !=[]:
                    maxa=np.max(nums)
                    for j in range(len(nums)):
                        if nums[j-len(temp)] == maxa:
                            temp.append(nums.pop(j-len(temp)))
                    max[i+1]=temp
            if len(max)<3:
                return max[1][0]
            else:
                return max[3][0]