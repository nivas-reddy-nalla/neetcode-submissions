class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams_map = {}

        for string in strs:
            sorted_string = "".join(sorted(string))

            if sorted_string in anagrams_map:
                anagrams_map[sorted_string].append(string)
            else:
                anagrams_map[sorted_string] = [string]
        
        return [anagrams_map[anagram] for anagram in anagrams_map]