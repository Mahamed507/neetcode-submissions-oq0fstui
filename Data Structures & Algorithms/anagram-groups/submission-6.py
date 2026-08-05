class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        group_ana = defaultdict(list)

        if strs is None:
            return [""]

        for s in strs:
            word = "".join(sorted(s))

            group_ana[word].append(s)


        return list(group_ana.values())

        


        

        '''
        understand
        1. input -> has a lst of strings.
        2. output -> returns a sublist of the same char. Does not matter the order.
        3. if str is empty return an empty array.


        match
        1. dict/hashmap 

        key:val
        alphebatcial order : [original elements]  <- val needs to be a lst. 


        plan
        1. create a empty dict called ' group_ana'
        2. if strs is None then return [""].
        3. for loop  , and sorted(i) , "".join(i) , group_ana[i] = str
        4. return group_ana.values()
        '''
        