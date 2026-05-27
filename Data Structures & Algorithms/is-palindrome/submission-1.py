class Solution:
    def isPalindrome(self, s: str) -> bool:
        sc = " ".join(ch.lower() for ch in s if ch.isalnum())
        
        return sc[::]==sc[::-1]