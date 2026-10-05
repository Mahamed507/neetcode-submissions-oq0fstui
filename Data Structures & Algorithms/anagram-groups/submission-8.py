class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        map = defaultdict(list)
       

        if strs == None:
            return ['']


        for s in strs:
           word = "".join(sorted(s))
           map[word].append(s)

           
           


        return list(map.values())
    
        