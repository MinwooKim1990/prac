import numpy
class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        if -2**31 <= dividend <= 2**31-1 and -2**31 <= divisor <= 2**31-1 and divisor !=0 :
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
        elif -2**31 > dividend or -2**31 > divisor:
            return -2**31
        elif 2**31-1 < dividend or 2**31-1 < divisor:
            return 2**31-1
        else:
            return 0
        
if __name__ == '__main__':
    # begin
    print(Solution().divide(-1021418889,1064910933))