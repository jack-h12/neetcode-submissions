class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        heights_dict = {}
        output = []
        for i in range(len(heights)):
            heights_dict[heights[i]] = names[i]
        
        descending_heights = sorted(heights, reverse=True)
        for i in range(len(descending_heights)):
            output.append(heights_dict[descending_heights[i]])
    
        return output