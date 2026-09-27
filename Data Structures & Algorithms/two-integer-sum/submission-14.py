class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        if nums == None:
            return []

        
        hashmap = {}
        values = 0

        for i , n in enumerate(nums):
            values = target - n

            if values in hashmap:
                return[hashmap[values] , i]

            else:
                hashmap[n] = i

        
            




        '''
        understand
        1. input - nums arry(int) and target(total val)
        2. output - return a lst of indices that add up the target.
        3. edge case - if nums is none.
        4. core logic - map(for quick lookup) , for loop and if statments. 

        plan
        1. check if nums array is None , then return an empty array.
        2. create a dict/HashMap and a empty list.
        3. for loop(use enumerate) , and inside the loop add the key(elemetns) and values(the index). so add it into the map.
        4. Inside the loop , if map[i] + map[i] == target , then 
          append inside the list.

        5. outside the loop , return the list. 

        '''
        