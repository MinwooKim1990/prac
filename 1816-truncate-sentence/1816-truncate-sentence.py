class Solution:
    def truncateSentence(self, s: str, k: int) -> str:
        ss=list(s)
        sss=''
        s=0
        i=0
        while s != k:
            sss= sss+ss[i]
            if ss[i] == ' ':
                s+=1
            if s == k :
                sss = sss[:len(sss)-1]
            i+=1
            if len(sss) == len(ss):
                return sss
        
        return sss