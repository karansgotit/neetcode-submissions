

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()#sorts in place
        result = []
        for i in range(len(nums)):
            l,r = i + 1,len(nums) - 1
            target = -(nums[i])
            if i >= 1 and nums[i] == nums[i - 1]:
                continue
            while l < r:
                if nums[l] + nums[r] == target:
                    result.append([nums[i],nums[l],nums[r]])
                    l += 1
                    r -=1
                    while l < r and (nums[l] == nums[l - 1] and nums[r] == nums[r + 1]):
                        l += 1
                        r -= 1
                elif nums[l] + nums[r] < target:
                    l += 1
                else:
                    r -=1
        return result


        
    





        