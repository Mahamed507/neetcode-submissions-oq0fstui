class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        if nums == []:
            return False

        map = {}

        for i in range(len(nums)):
            map[nums[i]] = 1 + map.get(nums[i] , 0)

            if map[nums[i]] > 1:
                return True


       

        return False


        '''
        understand
        1.input - > takes a nums(lst)
        2. output - > returns True if duplicate , otherwise its false. 
        3. edge case -> if nums is empty return false.
        4. core logic -> use a map, for loop.


        plan
        1. if nums is empty , return False.
        2. create a hashmap , call it 'map'.
        3. use a for loop to iterate through the elements. 
           
            add it into my map , map[] = 1 + map.get(map[] , 0)


        4. if map.values() > = 1 : return True


         return False
        '''
        