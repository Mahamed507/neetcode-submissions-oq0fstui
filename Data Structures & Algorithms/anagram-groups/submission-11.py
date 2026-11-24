class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        if strs == None:
            return [""]

        map = defaultdict(list)

        for s in strs:
            words = "".join(sorted(s))

            map[words].append(s)


        return list(map.values())

        '''
        understand
        1. input - strs(list of strings)
        2. output - returns into a sublist 
        3. edge case - strs is null.

        plan
        1. if strs is None , return empty string.
        2. create a map(string : list)
        3. for  loop 's' , 
            create a empty string var = "".join(s)
            then add it into the map key and values.

        4. return list(map.values())
        '''
        