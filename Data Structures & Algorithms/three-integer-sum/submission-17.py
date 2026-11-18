class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()

        ans = []
        for k in range(len(nums)):
            if nums[k] > 0:
                break
            if nums[k] == nums[k-1] and k > 0:
                continue
            
            target = -nums[k]
            i, j = k + 1, len(nums) - 1

            while i < j:
                if nums[i] + nums[j] == target:
                    ans.append([nums[i], nums[j], nums[k]])
                    i += 1
                    j -= 1

                    while nums[i] == nums[i - 1] and i < j:
                        i += 1
                    while nums[j] == nums[j + 1] and i < j:
                        j -= 1
                elif nums[i] + nums[j] < target:
                    i += 1
                else:
                    j -= 1
        
        return ans