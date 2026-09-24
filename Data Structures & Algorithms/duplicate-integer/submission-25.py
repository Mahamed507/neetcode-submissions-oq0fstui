class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:

        '''
        understand
        1. input - list of nums(int).
        2. output - returns True if more than one value appears in nums array.
        3.edge case - if nums array is null.
        5. core logic: map 

        plan
        1. if nums is None , return False
        2. create a map. 
        3. create a for loop to iterate through nums array.
        4. inside the loop , add the map(elements : freq)
        5. outside the loop , check if values is > 0, return True , otherwise return false.
        '''

        if nums is None:
            return False

        map = {}

        for i in range(len(nums)):
            map[nums[i]] = 1 + map.get(nums[i] , 0)

            if map[nums[i]] > 1:
                return True

        return False

          

       
        