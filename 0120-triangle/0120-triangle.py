import numpy as np
class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        if len(triangle) == 1:
            return triangle[0][0]
        dp=np.full((len(triangle), len(triangle[-1])), np.nan)
        dp[0][0]=triangle[0][0]
        res=[]
        def cal(a,b):
            if np.isnan(dp[a][b]):
                if b == 0:
                    dp[a][b] = dp[a-1][b] + triangle[a][b]
                elif b == len(triangle[a])-1:
                    dp[a][b] = dp[a-1][b-1] + triangle[a][b]
                else:
                    dp[a][b] = np.min([dp[a-1][b-1] + triangle[a][b], dp[a-1][b] + triangle[a][b]])
            return dp[a][b]
        for i in range(len(triangle)-1):
            i=i+1
            for j in range(len(triangle[i])):
                if i == len(triangle)-1:
                    res.append(cal(i,j))
                else:
                    cal(i,j)
        return int(np.min(res))