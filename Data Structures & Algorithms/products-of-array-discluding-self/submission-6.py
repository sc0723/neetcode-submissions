class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        ans = []
        # Compute left product
        curr_left = 1
        ans.append(1)
        for i in range(1, len(nums)):
            curr_left *= nums[i-1]
            ans.append(curr_left)

        # Multiply current right
        curr_right = 1
        ans[len(nums) - 1] *= curr_right
        for j in range(len(nums)-2, -1, -1):
            curr_right *= nums[j + 1]
            ans[j] *= curr_right

        return ans