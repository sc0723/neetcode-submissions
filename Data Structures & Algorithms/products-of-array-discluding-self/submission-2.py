class Solution:
    
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        leftProd = 1
        rightProd = 1
        res = [1] * len(nums)

        for i in range(len(nums)):
            res[i] = leftProd
            leftProd *= nums[i]
        
        for j in range(len(nums)-1, -1, -1):
            res[j] *= rightProd
            rightProd *= nums[j]
        
        return res


    