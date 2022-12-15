import numpy as np
class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        max=np.max(arr)
        maxind=arr.index(max)
        arr=np.array(arr)
        incl=arr[:maxind]
        decl=arr[maxind:-1]
        compin=arr[1:maxind+1]
        compde=arr[maxind+1:]

        if all(i < 0 for i in (incl-compin)) and all(i > 0 for i in (decl-compde)) and list(incl-compin)!=[] and list(decl-compde)!=[]:
            return True
        else :
            return False