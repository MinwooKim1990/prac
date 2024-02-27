class Solution:
    def countBits(self, n: int) -> List[int]:
        ans=[bin(i)[2:] for i in range(n+1)]
        ans2=[]
        for i in ans:
            ans2.append(sum(list(map(int,list(i)))))
        return ans2