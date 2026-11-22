class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        if strs == None:
            return [""]

        map = defaultdict(list)

        for s in strs:
            word = "".join(sorted(s))

            map[word].append(s)

        return list(map.values())
        

     


      

    