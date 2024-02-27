# 1. ans[i >> 1]: This part takes the number i, shifts it right by 1 bit (which is the same as dividing by 2),
#    and uses the result to find out how many '1's were in the binary representation of this new number.
#    Since we are shifting right by 1, we effectively ignore the last bit of i for this operation.
#    This means if i was 4 (binary '100'), i >> 1 would be 2 (binary '10'), and we look up how many '1's
#    are in the number 2 from our previously calculated answers.

# 2. (i & 1): This part checks if i is odd or even. It does this by ANDing i with 1, which only looks at the
#    least significant bit of i. If i is odd, this bit will be '1', and the result of (i & 1) will be 1.
#    If i is even, the bit will be '0', and the result will be 0. This effectively counts an extra '1' if i is odd,
#    since odd numbers have a '1' in the least significant bit of their binary representation.
class Solution:
    def countBits(self, n: int) -> List[int]:
        ans = [0] * (n + 1)
        for i in range(1, n + 1):
            
            ans[i] = ans[i >> 1] + (i & 1)
        return ans
