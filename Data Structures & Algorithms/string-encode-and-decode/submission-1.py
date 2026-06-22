class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_string = ""
        for string in strs:
            encoded_string += string
            encoded_string += "是"
        return encoded_string

    def decode(self, s: str) -> List[str]:
        decoded_strs = []
        curr_str = ""
        for char in s:
            if char == "是":
                decoded_strs.append(curr_str)
                curr_str = ""
            else:
                curr_str += char
        return decoded_strs
