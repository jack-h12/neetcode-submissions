# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        l = 1
        r = n
        our_guess = (l + r) // 2
        while guess(our_guess) != 0:
            if guess(our_guess) == -1:
                r = our_guess - 1
                our_guess = (l + r) // 2
            else:
                l = our_guess + 1
                our_guess = (l + r) // 2
        return our_guess