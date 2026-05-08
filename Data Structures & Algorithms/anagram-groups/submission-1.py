class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = {}
        for string in strs:
            hash_val = self.anagram_hash_prime(string)
            if hash_val in result:
                result[hash_val].append(string)
            else:
                result[hash_val] = [string]
        return list(result.values())
    
    def anagram_hash_prime(self, s: str) -> int:
        """
        Collision-resistant anagram hash using unique prime numbers per character.
        All anagrams produce the same product; non-anagrams almost certainly differ.
        """
        # First 26 prime numbers mapped to a–z
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


        