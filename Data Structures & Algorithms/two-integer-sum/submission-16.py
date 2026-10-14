class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        track = {}

        for i in range(len(nums)):
            if nums[i] in track:
                ans = [track[nums[i]], i]
                return ans
            track[target - nums[i]] = i