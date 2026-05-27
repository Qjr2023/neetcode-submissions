class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        counts = [0] * 26
        for c in s:
            i = ord(c) - ord("a")
            counts[i] += 1
        
        for c in t:
            i = ord(c) - ord("a")
            counts[i] -= 1
        
        for i in range(len(counts)):
            if counts[i] != 0:
                return False
        
        return True
                


        