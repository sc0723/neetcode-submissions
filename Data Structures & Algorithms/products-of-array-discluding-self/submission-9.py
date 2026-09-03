class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        ans = [1]

        curr_left = 1

        for i in range(1, len(nums)):
            curr_left *= nums[i-1]
            ans.append(curr_left)

        curr_right = 1
        
        for j in range(len(nums)-2, -1, -1):
            curr_right *= nums[j+1]
            ans[j] *= curr_right

        return ans