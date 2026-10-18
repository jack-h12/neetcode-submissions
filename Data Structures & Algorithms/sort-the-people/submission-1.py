class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        heights_dict = {}
        output = []
        for i in range(len(heights)):
            heights_dict[heights[i]] = i
        
        for i in range(len(heights_dict) -1, -1, -1):
            output.append(names[heights_dict[max(heights_dict)]])
            heights_dict.pop(max(heights_dict))
    
        return output