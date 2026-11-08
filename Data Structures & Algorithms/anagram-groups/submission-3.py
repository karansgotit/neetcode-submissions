class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dict = {}# string to string list mapping
        for s in strs:
            sorted_s = "".join(sorted(s))
            if sorted_s not in dict:
                dict[sorted_s] = []
                dict[sorted_s].append(s)
            else:#key exists
                dict[sorted_s].append(s)
        return list(dict.values())





            
            

            
        
        
        