class Solution:

    def encode(self, strs: List[str]) -> str:
        result = []
        for string in strs:
            result.append(str(len(string))+ "#" + string)
        return "".join(result)

    def decode(self, s: str) -> List[str]:
        i = 0
        result = []
        while i < len(s):
            j = i
            while s[j] != "#":
                j+=1
            
            length = int(s[i:j])
            result.append(s[j+1: j+length+1])
            i = j+length+1
        
        return result