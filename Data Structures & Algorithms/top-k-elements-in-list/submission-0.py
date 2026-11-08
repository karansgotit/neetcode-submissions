from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        countMap = Counter(nums)
        tupleList = countMap.most_common(k)
        result = []
        for tup in tupleList:
            result.append(tup[0])
        return result

        