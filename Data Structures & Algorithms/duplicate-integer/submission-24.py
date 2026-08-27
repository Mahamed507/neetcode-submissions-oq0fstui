class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:

        if nums is None:
            return False

        map = {}

        for i in range(len(nums)):
            map[nums[i]] = 1 + map.get(nums[i] , 0)

            if map[nums[i]] > 1:
                return True


        return False


           


        






           

        '''
        plan
        1. check if the nums array is empty, and return false. 
        2. create a empty hashmap. 
        3. use a for loop , and then append it into the map(increment the values if you come accoss the same value again.).
        4. use a if statment and find if map.values() > 1 , return true  , else return false.



        '''
        