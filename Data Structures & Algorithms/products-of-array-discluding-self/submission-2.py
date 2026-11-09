class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left,right = [1] * len(nums),[1] * len(nums)
        output = [1] * len(nums)
        for i in range(1,len(left)):
            left[i] = left[i - 1] * nums[i - 1]
        for k in range(len(right) - 2,-1,-1):
            right[k] = right[k + 1] * nums[k + 1]
        for j in range(len(output)):
            output[j] = left[j] * right[j]
        return output
    
    
    



        