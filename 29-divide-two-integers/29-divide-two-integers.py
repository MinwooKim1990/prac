import numpy
class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
          e=abs(dividend)
          s=abs(divisor)
          i = numpy.exp(numpy.log(e)-numpy.log(s))
          print(i)
          if dividend<0 and divisor>0:
            i=numpy.int(numpy.ceil(-i))
          elif dividend>0 and divisor<0:
            i=numpy.int(numpy.ceil(-i))
          else:
            i=numpy.int(numpy.round(i))
          if i > 2**31-1:
              i=2**31-1
          elif i < -2**31:
              i=-2**31
          if abs(numpy.round(numpy.exp(numpy.log(i)+numpy.log(s))))>abs(dividend):
            i=i-1
          return i
if __name__ == '__main__':
    # begin
    print(Solution().divide(-1021418889,1064910933))
        
if __name__ == '__main__':
    # begin
    print(Solution().divide(-1021418889,1064910933))