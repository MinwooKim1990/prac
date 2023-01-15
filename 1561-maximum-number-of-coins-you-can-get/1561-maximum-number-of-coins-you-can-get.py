class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort(reverse=True)
        res=[]
        print(piles)
        while piles !=[]:
            del piles[0]
            res.append(piles.pop(0))
            del piles[-1]
        return sum(res)