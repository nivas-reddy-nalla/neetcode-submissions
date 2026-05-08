class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        s1_hash = self.anagram_hash_prime(s1)
        left, right = 0, len(s1)
        window_hash = self.anagram_hash_prime(s2[left:len(s1)])

        while right<len(s2):
            if window_hash == s1_hash:
                return True
            else:
                prev_hash  = self.anagram_hash_prime(s2[left])
                next_hash = self.anagram_hash_prime(s2[right])
                window_hash = (window_hash//prev_hash)*next_hash
                left+=1
                right+=1
        if window_hash == s1_hash:
            return True
        return False
    def anagram_hash_prime(self, s: str) -> int:
        primes = [
            2,  3,  5,  7, 11, 13, 17, 19, 23, 29,
            31, 37, 41, 43, 47, 53, 59, 61, 67, 71,
            73, 79, 83, 89, 97,101
        ]

        s = s.lower().replace(" ", "")

        result = 1
        for c in s:
            if c.isalpha():
                result *= primes[ord(c) - ord('a')]
        return result