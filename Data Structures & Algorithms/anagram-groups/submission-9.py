class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        if strs == None:
            return [""]

        map = defaultdict(list)

        for s in strs:
            word = "".join(sorted(s))
            map[word].append(s)


        return list(map.values())



        '''
        plan
        1. if strs(list) is None then return empty sublist string.
        2. create a map(sorted word : list)
        3. use a for loop , 
             word = sort the str and then join. 
             map[word].append(s)


        4. return list(map.values())
        '''
        