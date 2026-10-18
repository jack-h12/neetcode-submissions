class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        heights_dict = {}
        output = []
        for i in range(len(heights)):
            heights_dict[heights[i]] = i
        
        for i in range(len(heights_dict) -1, -1, -1):
            curr_max_height = max(heights_dict)
            output.append(names[heights_dict[curr_max_height]])
            heights_dict.pop(curr_max_height)
    
        return output