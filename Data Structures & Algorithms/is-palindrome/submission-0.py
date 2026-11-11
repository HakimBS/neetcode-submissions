class Solution:
    def isPalindrome(self, s: str) -> bool:
        ch = ''
        for c in s:
            if c.isalnum():
                ch += c.lower()
        return ch==ch[::-1]

        
        