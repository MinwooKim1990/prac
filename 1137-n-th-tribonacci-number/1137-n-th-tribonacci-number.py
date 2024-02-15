class Solution:
    def tribonacci(self, n: int) -> int:
        if n==0:
            return 0
        elif n==1:
            return 1
        elif n==2:
            return 1
        else:
            dp=[[] for _ in range(n+1)]
            dp[0]=0
            dp[1]=1
            dp[2]=1
            def tri(n):
                if dp[n-1] != []:
                    t_1=dp[n-1]
                else:
                    t_1=tri(n-1)
                if dp[n-2] != []:
                    t_2=dp[n-2]
                else:
                    t_2=tri(n-2)
                if dp[n-3] != []:
                    t_3=dp[n-3]
                else:
                    t_3=tri(n-3)
                dp[n]=t_1+t_2+t_3
                return dp[n]
            return tri(n)