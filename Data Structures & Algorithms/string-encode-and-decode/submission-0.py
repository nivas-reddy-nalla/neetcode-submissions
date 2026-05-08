class Solution:

    def encode(self, strs: List[str]) -> str:
        result = []
        for string in strs:
            n = len(string)
            result.append(str(n) + '#' + string)

        return "".join(result)

    def decode(self, s: str) -> List[str]:

        result = []
        i = 0

        while i < len(s):
            # Find the position of the next '#'
            j = s.find('#', i)
            length = int(s[i:j])  # Get the length of the string
            string = s[j+1:j+1+length]  # Extract the string
            result.append(string)
            i = j + 1 + length  # Move to the next encoded string

        return result


