class Solution:
    def reverseBits(self, n: int) -> int:
        ans = 0 

        for i in range(32):
            if (n>>i & 1):
                ans += 2**(32-(i+1))
        return ans