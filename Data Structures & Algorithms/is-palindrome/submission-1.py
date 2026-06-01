class Solution:
    def isPalindrome(self, s: str) -> bool:
        alnum_chars = []
        for c in s:
            if c.isalnum():
                alnum_chars.append(c)
        alnum_chars = "".join(alnum_chars)
        if len(alnum_chars) % 2 == 0:
            first_half = alnum_chars[:(len(alnum_chars)//2)]
            second_half = alnum_chars[(len(alnum_chars)//2):]
        else:
            first_half = alnum_chars[:(len(alnum_chars)//2)]
            second_half = alnum_chars[(len(alnum_chars)//2) + 1:]
        print(first_half.lower())
        print(second_half[::-1].lower())
        if first_half.lower() == second_half[::-1].lower():
            return True
        else:
            return False
        