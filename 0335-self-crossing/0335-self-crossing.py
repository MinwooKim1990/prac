class Solution:
    #def isSelfCrossing(self, distance: List[int]) -> bool:
    #    a=[[0,0]]
    #    for i in range(len(distance)):
    #        b=a[-1]
    #        if i % 4 == 0:
    #            temp=list(range(distance[i]+1))[1:]
    #            for j in range(len(temp)):
    #                t=[b[0],b[1]+temp[j]]
    #                if t in a:
    #                    return True
    #                a.append(t)
    #        if i % 4 == 1:
    #            temp=list(range(distance[i]+1))[1:]
    #            for j in range(len(temp)):
    #                t=[b[0]-temp[j],b[1]]
    #                if t in a:
    #                    return True
    #                a.append(t)
    #        if i % 4 == 2:
    #            temp=list(range(distance[i]+1))[1:]
    #            for j in range(len(temp)):
    #                t=[b[0],b[1]-temp[j]]
    #                if t in a:
    #                    return True
    #                a.append(t)
    #        if i % 4 == 3:
    #            temp=list(range(distance[i]+1))[1:]
    #            for j in range(len(temp)):
    #                t=[b[0]+temp[j],b[1]]
    #                if t in a:
    #                    return True
    #                a.append(t)
    #    return False
    
    def isSelfCrossing(self, x):
        b = c = d = e = 0
        for a in x:
            if d >= b > 0 and (a >= c or a >= c-e >= 0 and f >= d-b):
                return True
            b, c, d, e, f = a, b, c, d, e
        return False