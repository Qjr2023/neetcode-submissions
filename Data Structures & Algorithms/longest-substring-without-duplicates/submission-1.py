class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char_index = {}
        l = 0
        max_len = 0

        for r, char in enumerate(s):
            if char in char_index and char_index[char] >= l:
                # 遇到重复字符，移动左指针到上次出现的下一个位置
                l = char_index[char] + 1

            # 更新字符最后出现的位置
            char_index[char] = r

            # 更新最大长度
            max_len = max(max_len, r - l + 1)

        return max_len