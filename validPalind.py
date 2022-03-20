class Solution:
    def isPalindrome(self, s: str) -> bool:
        new_string = ''.join(char for char in s.lower() if char.isalnum())
        return (new_string==new_string[::-1])