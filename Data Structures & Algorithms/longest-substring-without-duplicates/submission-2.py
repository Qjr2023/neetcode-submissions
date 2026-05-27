class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        mapC = {}
        res = 0

        for r, c in enumerate(s):
            if c in mapC and mapC[c] >= l:
                l = mapC[c] + 1
            mapC[c] = r
            res = max(res, r - l + 1)
        return res
        