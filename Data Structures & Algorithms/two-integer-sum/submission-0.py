class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        save_num = {}
        
        for i in range(len(nums)):
            diff = target - nums[i]
            if diff in save_num:
                return [save_num[diff], i]
            save_num[nums[i]] = i



        