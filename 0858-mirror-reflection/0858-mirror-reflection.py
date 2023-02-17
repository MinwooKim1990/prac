class Solution:
    def mirrorReflection(self, p: int, q: int) -> int:
        if p%q==0:
            if (p/q)%2==0:
                return 2
            else :
                return 1
        else:
            n=2
            while (q*n) % p != 0:
                n+=1
            if (q*n/p)%2 == 0:
                return 0
            else:
                if n%2 == 0:
                    return 2
                else:
                    return 1
    