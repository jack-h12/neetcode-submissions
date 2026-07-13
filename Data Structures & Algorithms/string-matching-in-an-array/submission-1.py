class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        output = []
        for i in range(len(words)):
            word = words[i]
            words[i] = ""
            for j in range(len(words)):
                if word in words[j]:
                    output.append(word)
                    break
            words[i] = word
        return output