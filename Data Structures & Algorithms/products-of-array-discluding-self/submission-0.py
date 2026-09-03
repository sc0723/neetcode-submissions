class Solution:
    
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # currProd = 1
        res = [0] * len(nums)
        # for i in range(len(nums)):
        #     currProd *= nums[i]
        
        # for i in range(len(nums)):
        #     if nums[i] == 0:
        #         res[i] = currProd
        #     else:
        #         res[i] = int(currProd / nums[i])
        
        # return res
        for i in range(len(nums)):
            t = nums.copy()
            t.pop(i)
            res[i] = self.calcProduct(t)
        return res
    def calcProduct(self, temp):
        prod = 1
        for i in temp:
            prod *= i
        return prod
    