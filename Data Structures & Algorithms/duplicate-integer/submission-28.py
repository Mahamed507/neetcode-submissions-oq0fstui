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
        1. input - arr as input
        2. output - reutrn true if duplicate.
        3. edge case - num is none.

        plan
        1. if nums is none , then return false.
        2. create a map
        3. for loop , 
             add the elements in the map.

             if map[i] is > 1 then return false. 
        '''
        