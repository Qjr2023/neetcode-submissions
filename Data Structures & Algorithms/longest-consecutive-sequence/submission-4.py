class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        nums.sort()
        res = 1
        length = 1
        for i in range(1, len(nums)):
            if nums[i] == nums[i - 1] + 1:
                length += 1
                res = max(res, length)
            elif nums[i] == nums[i - 1]:
                continue
            else:
                length = 1
        return res

