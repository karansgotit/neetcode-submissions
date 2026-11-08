class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashMap = {} #this has the value and its index
        for index,value in enumerate(nums):
            diff = target - value
            if diff in hashMap:
                return [hashMap[diff],index]
            hashMap[value] = index
        return




       



        