class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        freq = {}
        left = 0
        max_freq = 0
        result = 0

        for right in range(len(s)):
            # Add current character to frequency map
            freq[s[right]] = freq.get(s[right], 0) + 1
            max_freq = max(max_freq, freq[s[right]])

            # Check if window is valid
            while (right - left + 1) - max_freq > k:
                freq[s[left]] -= 1
                left += 1

            # Update result
            result = max(result, right - left + 1)

        return result