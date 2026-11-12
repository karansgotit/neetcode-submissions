from collections import Counter

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        numCounter = Counter(nums)
        result = []
        finalResult =[]
        for i in range(len(nums)):
            for j in range(i + 1,len(nums)):
                target = -(nums[i] + nums[j])
                numCounter[nums[i]] -= 1
                numCounter[nums[j]] -= 1
                if numCounter[target] > 0:
                    triplet = sorted([nums[i],nums[j],target])
                    if triplet not in result:
                        result.append(triplet)
                numCounter[nums[i]] += 1
                numCounter[nums[j]] += 1
        return result
    





        