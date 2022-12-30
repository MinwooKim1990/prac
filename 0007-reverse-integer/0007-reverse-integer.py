class Solution:
    def reverse(self, x: int) -> int:
        res=0
        if x < 0:
            s=-1
            x=s*x
        else:
            s=1
        lis=[int(i) for i in str(x)]
        dig=len(lis)
        for i in range(dig):
            res+=lis[i]*10**(i)
        if -2**31 <= res*s and res*s <=2**31-1:
            return res*s
        else:
            return 0        