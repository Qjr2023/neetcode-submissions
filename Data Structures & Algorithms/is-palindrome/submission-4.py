class Solution:
    def isPalindrome(self, s: str) -> bool:
        newS = ""
        for c in s:
            if c.isalnum():
                newS += c.lower()
        
        n = len(newS)
        for i in range(n // 2):
            if newS[i] != newS[n - 1 - i]:
                return False
        
        return True