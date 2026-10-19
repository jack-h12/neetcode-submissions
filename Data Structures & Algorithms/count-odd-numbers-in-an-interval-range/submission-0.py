class Solution:
    def countOdds(self, low: int, high: int) -> int:
        if low == high and low % 2 == 0:
            return 0
        else:
            return (high - low) // 2 + 1
            
        