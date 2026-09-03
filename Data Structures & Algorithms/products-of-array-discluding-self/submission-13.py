class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        ans = [1]

        prod_left = 1

        for i in range(1, len(nums)):
            prod_left *= nums[i-1]
            ans.append(prod_left)
        prod_right = 1
        for j in range(len(nums)-2, -1, -1):
            prod_right *= nums[j+1]
            ans[j] *= prod_right
        
        return ans