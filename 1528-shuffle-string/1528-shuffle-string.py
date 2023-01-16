class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        s=list(s)
        res=[0]*len(indices)
        for i in range(len(indices)):
            res[indices[i]]=s[i]  
        ress = ''.join([str(j) for j in res])
        return ress