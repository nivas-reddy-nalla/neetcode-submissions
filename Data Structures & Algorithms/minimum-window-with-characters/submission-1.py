class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t)>len(s) or t == "":
            return ""

        window = defaultdict(int)
        count_t = Counter(t)
        l = 0
        have, need = 0, len(count_t)
        res, resLen = [-1, -1], float("infinity")

        for r in range(len(s)):
            c = s[r]
            window[c]+=1

            if c in count_t and window[c] == count_t[c]:
                have+=1
            
            while have == need:
                if r-l+1 < resLen:
                    resLen = r-l+1
                    res = [l, r]
                window[s[l]]-=1
                if s[l] in count_t and window[s[l]]< count_t[s[l]]:
                    have-=1
                l+=1
        
        return s[res[0]: res[1]+1] if resLen != float("infinity") else ""
