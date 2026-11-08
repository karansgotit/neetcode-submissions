class Solution:
    def encode(self, strs: List[str]) -> str:
        encoded_string=""
        for s in strs:
            length = len(s)
            encoded_string += str(length)
            encoded_string += "#"
            encoded_string += s
        return encoded_string

    def decode(self, s: str) -> List[str]:
        decoded_string = []
        newString = s
        while len(newString) != 0:
            i = newString.find("#")
            length = int(newString[0:i])
            decoded_string.append(newString[i + 1:i + 1 + length])
            newString = newString[i + 1 + length : len(newString)]
        return decoded_string
            

