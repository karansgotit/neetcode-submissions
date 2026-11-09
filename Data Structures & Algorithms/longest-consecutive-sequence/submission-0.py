class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        longestLength = 0
        for num in numSet:
            startingPoint = False
            if num - 1 not in numSet:
                startingPoint = True
            if startingPoint == True:
                i = num
                j = 1
                while i + 1 in numSet:
                    j += 1
                    i += 1
                longestLength = max(longestLength,j)
        return longestLength


        