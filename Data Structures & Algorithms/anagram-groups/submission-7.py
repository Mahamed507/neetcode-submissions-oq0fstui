class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        if str is None:
            return ['']


        map = defaultdict(list)

  

        for w in strs:
            word = "".join(sorted(w))

            map[word].append(w)

        return list(map.values())


 



        '''
        plan
        1. Check if str array is empty.
        2. create a empty map.
        3. use a for loop , create a varaible called word and I want to sort the strings and add it into my values. 
        then inside the loop i want to also add it into the map of values for the orginal strings of the array.


        then return
        '''
        