from collections import Counter

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not s or not t:
            return ""

        t_map = Counter(t)
        window = {}
        have, need = 0, len(t_map)
        res, res_len = [-1, -1], float("inf")
        left = 0

        for right in range(len(s)):
            char = s[right]
            window[char] = window.get(char, 0) + 1

            if char in t_map and window[char] == t_map[char]:
                have += 1

            while have == need:
                # Update result
                if (right - left + 1) < res_len:
                    res = [left, right]
                    res_len = right - left + 1

                # Shrink window
                window[s[left]] -= 1
                if s[left] in t_map and window[s[left]] < t_map[s[left]]:
                    have -= 1
                left += 1

        l, r = res
        return s[l:r+1] if res_len != float("inf") else ""
