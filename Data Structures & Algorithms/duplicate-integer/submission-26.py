class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:

        '''
        understand
        1. input - nums array(int)
        2. output - return True if duplicate , return false
        3. edge case - if nums is none.
        4. core logic - use hashmap(element : freq)
        plan
        1. if nums is None  , return False.
        2. create a map 
        3. use a for loop ,
              add it into the map

              if map[i] is > 1 then  return True

        else return False
        '''

        if nums == None:
            return False

        maps = {}

        for e in nums:
            maps[e] = 1 + maps.get(e , 0)

            if maps[e] > 1:
                return True


        return False
        