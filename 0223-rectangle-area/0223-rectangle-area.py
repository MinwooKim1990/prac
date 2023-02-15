import numpy as np
class Solution:
    def computeArea(self, ax1: int, ay1: int, ax2: int, ay2: int, bx1: int, by1: int, bx2: int, by2: int) -> int:
        a1=np.linspace(ax1,ax2,abs(ax1-ax2)+1)
        a2=np.linspace(bx1,bx2,abs(bx1-bx2)+1)
        b1=np.linspace(ay1,ay2,abs(ay1-ay2)+1)
        b2=np.linspace(by1,by2,abs(by1-by2)+1)
        ina=sorted(list(set(a1).intersection(a2)))
        inb=sorted(list(set(b1).intersection(b2)))
        tot=abs(ax2-ax1)*abs(ay2-ay1)+abs(bx2-bx1)*abs(by2-by1)
        if ina != []:
            if inb != []:
                ints=int(abs(ina[-1]-ina[0])*abs(inb[-1]-inb[0]))
                return tot-ints
        return tot