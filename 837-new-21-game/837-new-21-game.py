# Dynamic Programming mathod Like fibonachi series
# P( X = 0 ) = 1                            Initial state, no need to draw cards
# P( X = 1 ) = 1/W                          Only 1 out of W chance in getting X = 1
# P( X = 2 ) = 1/W + 1/W^2                  We can draw a 2 or two 1s.
# P( X = 3 ) = 1/W + 1/W^2 + 1/W^2 + 1/W^3  We can draw a 3, a (2,1), a (1,2), and three 1s. 
# P( X = 4 ) = ( P( X = 3 ) + P( X = 2 ) + P( X = 1 )) / W

class Solution:
    def new21Game(self, n: int, k: int, maxPts: int) -> float:
        if k == 0 or k + maxPts <= n :
          return 1
        prob=[1]+[0]*n  # make vacant cache
        result=0
        sum=1
        for i in range(n):
          prob[i+1]=sum/maxPts
          #print('i, dp',i+1,prob)
          if i+1<k:
            sum=sum+prob[i+1]
          else:
            result=result+prob[i+1]
          if i+1-maxPts>=0:
            sum=sum-prob[i+1-maxPts] # for exclude not reaching probability
        return result

if __name__ == '__main__':
  print(Solution().new21Game(21,17,10))
"""
# Monte-Carlo mathod
pre=7
p=3
class Solution:
    def new21Game(self, n: int, k: int, maxPts: int) -> float:
        win = 0
        for i in range(10**pre*p):
            alice = 0
            while alice < k:
                trial = np.random.randint(maxPts)+1
                alice = alice + trial
            if alice <= n:
                win=win+1
        return win/(10**pre*p)

if __name__ == '__main__':
  print(Solution().new21Game(21,17,10))"""
