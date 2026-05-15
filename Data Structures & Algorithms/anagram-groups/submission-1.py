class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # do this if map , when every key has it's list in value. 
        res = defaultdict(list)

        for s in strs:
            sortedS = ''.join(sorted(s))
            res[sortedS].append(s)
        return list(res.values())
       



    
            


       
        

        

        