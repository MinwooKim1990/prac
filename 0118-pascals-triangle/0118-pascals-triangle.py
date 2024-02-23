class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        out=[]
        for i in range(1,numRows+1):
            temp=[]
            if i == 1:
                out.append([1])
            elif i == 2 :
                out.append([1,1])
            else:
                temp=[1 for a in range(i)]
                key=int(i/2)
                for j in range(i-2):
                    temp[j+1]=out[i-2][j+1]+out[i-2][j]
                if i % 2 == 0:
                    temp[key:]=sorted(temp[:key], reverse=True)
                else:
                    temp[key:]=sorted(temp[:key+1], reverse=True)
                out.append(temp)
        return out
                        
                
                