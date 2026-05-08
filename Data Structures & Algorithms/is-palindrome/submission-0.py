class Solution:
    def isPalindrome(self, s: str) -> bool:

        formatted_string_list = []

        for char in s:
            if char.isalnum():
                formatted_string_list.append(char.lower())

        left, right = 0, len(formatted_string_list)-1

        while left<right:
            if formatted_string_list[left] == formatted_string_list[right]:
                left+=1
                right-=1
            else:
                return False
        return True