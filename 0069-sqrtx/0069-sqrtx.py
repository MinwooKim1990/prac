class Solution:
    def mySqrt(self, x: int) -> int:
        if x==1:
            return 1
        a=x/2
        b=0
        if 0<=a*a-x<1:
            return int(a)
        else:
            while a*a-x>=1:
                b=a-((a*a-x)/(2*a))
                a=b
            return int(a)
        
        