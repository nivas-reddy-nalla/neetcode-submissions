class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        start, end = 0, 0
        n = len(s)

        seen = set()
        ans = 0
        while end<n:
            if s[end] in seen:
                ans = max(ans, end-start)
                while s[end] in seen:
                    seen.remove(s[start])
                    start+=1
            seen.add(s[end])
            end+=1
        ans = max(ans, end-start)
        return ans
                

