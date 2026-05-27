class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)
        l, r = 0, n - 1
        mid = (n - 1) // 2

        while l <= r:
            if target == nums[mid]:
                return mid
            elif target < nums[mid]:
                r = mid - 1
                mid = (r + l) // 2
            else:
                l = mid + 1
                mid = (r + l) // 2
        
        return -1
