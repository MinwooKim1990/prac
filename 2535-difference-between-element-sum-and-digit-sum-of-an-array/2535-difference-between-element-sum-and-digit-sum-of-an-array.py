class Solution:
    def differenceOfSum(self, nums: List[int]) -> int:
        res=0
        for i in nums:
            if i >= 10:
                a=i//1000
                b=(i-a*1000)//100
                c=(i-a*1000-b*100)//10
                d=i-a*1000-b*100-c*10
                res+=(i-(a+b+c+d))

        return res