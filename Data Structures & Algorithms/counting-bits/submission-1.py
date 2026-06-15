class Solution:
    def countBits(self, n: int) -> List[int]:
        lst = []
        for i in range(n+1):
            count = self.numOfOnes(i)
            lst.append(count)
        return lst
        
    
    def numOfOnes(self, n):
        count = 0
        while n != 0:
            if n % 2 == 1:
                count += 1
            n = n >> 1
        return count