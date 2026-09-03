class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        i = 0
        j = len(numbers)-1
        curr = target + 1
        while curr != target:
            curr = numbers[i] + numbers[j]
            if curr < target:
                i+=1
            elif curr > target:
                j-=1
        
        return [i+1, j+1]