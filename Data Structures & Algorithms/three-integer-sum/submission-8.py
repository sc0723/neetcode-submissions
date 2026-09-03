class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()

        for i in range(len(nums)):
            if nums[i] > 0:
                break
            
            if nums[i] == nums[i-1] and i > 0:
                continue
            
            j = i + 1
            k = len(nums)-1
            target = -nums[i]
            while j < k:
                curr_sum = nums[j] + nums[k]
                if curr_sum == target:
                    res.append([nums[i], nums[j], nums[k]])
                    j += 1
                    k -= 1
                    while nums[j] == nums[j - 1] and j < k:
                        j += 1
                elif curr_sum < target:
                    j += 1
                else:
                    k -= 1
        
        return res