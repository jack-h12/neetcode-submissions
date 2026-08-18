class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        found = False
        added_value = False
        output = []
        for i in range(len(nums1)):
            for j in range(len(nums2)):
                if found == True:
                    if nums2[j] > nums1[i]:
                        output.append(nums2[j])
                        found = False
                        added_value = True
                        break
                if nums2[j] == nums1[i]:
                    found = True
            if added_value == False:
                output.append(-1)
            added_value = False
        return output