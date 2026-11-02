class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        if nums == None:
            return False

        map = {}

        for i in nums:
            map[i] = 1 + map.get(i , 0)

            if map[i] > 1:
                return True

        return False

      

     

        '''
        understand
        1. input - takes a list of int
        2. output - return True if duplicate , otherwise return false. 
        3. edge case - if nums is null.
        
        plan
        1. check if nums array is None , and if it is then return false.
        2. create a empty map(elemetns : freq)

        3. use a for loop ,
              add it into the map
              then, if map values is > 0
                       then return true

        4. return false. 
        '''
        