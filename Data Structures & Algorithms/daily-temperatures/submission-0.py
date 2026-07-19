class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = []
        for i in range(len(temperatures)):
            if i == len(temperatures) - 1:
                result.append(0)
                break
            curr_temp = temperatures[i]
            for j in range(i+1, len(temperatures)):
                if temperatures[j] > curr_temp:
                    result.append(j - i)
                    break
                if j == len(temperatures) - 1:
                    result.append(0)
                    break
        return result