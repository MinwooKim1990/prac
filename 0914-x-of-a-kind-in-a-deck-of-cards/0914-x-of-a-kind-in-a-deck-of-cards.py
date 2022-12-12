import numpy as np
class Solution:
    def hasGroupsSizeX(self, deck: List[int]) -> bool:
        wht=[]
        while deck!=[]:
            a=deck[0]
            copy=len(deck)
            tmp=[]
            for i in range(copy):
                if a == deck[i-len(tmp)]:
                    deck.pop(i-len(tmp))
                    tmp.append(1)
            wht.append(len(tmp))
        min=np.min(wht)
        wht2=[]
        di=[]
        dic={}
        for j in range(len(wht)):
            if wht[j] == 1:
                return False
        for j in range(min):
            if min%(j+2) == 0:
                di.append(j+2)
        for j in range(len(di)):
            temp=[]
            for i in range(len(wht)):
                if wht[i]%di[j]==0:
                    temp.append(1)
            dic[j]=temp
        for i in range(len(dic)):
            if sum(dic[i]) == len(wht):
                return True
        return False