class Solution:
    def isPalindrome(self, s: str) -> bool:
        sc = " ".join(ch.lower() for ch in s if ch.isalnum())
        length = (len(sc) - 1) // 2
        for i in range(length):
            if sc[i] != sc[len(sc) - 1 - i]:
                return False
        return True