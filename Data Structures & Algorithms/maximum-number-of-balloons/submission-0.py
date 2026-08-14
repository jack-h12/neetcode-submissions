class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        letter_count = {"b" : 0, "a" : 0, "l" : 0, "o" : 0, "n" : 0}
        for i in range(len(text)):
            if text[i] in letter_count.keys():
                letter_count[text[i]] += 1
        letter_count['l'] = letter_count['l'] // 2
        letter_count['o'] = letter_count['o'] // 2
        return min(letter_count.values())
        