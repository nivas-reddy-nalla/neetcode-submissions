class Solution:
    def countBits(self, n: int) -> List[int]:
        result = [0]*(n+1)

        for i in range(n+1):
            result[i] = self.countSetBits(i)
        return result
        
    def countSetBits(self, n: int) -> int:
        count = 0

        for i in range(32):
            if (n>>i & 1):
                count+=1
        return count