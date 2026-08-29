class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        if nums is None:
            return []


        map = {}

        values = 0

        for i , n in enumerate(nums):
            values = target - n
            if values in map:
               return [map[values] , i]


            map[n] = i


        return []


            

        


        '''
        plan
        1. check if nums array is None and return [].
        2. create a map 
        3. then use a for loop and enumerate and add it into the map.
        4. then check if the n is in map add it into the list 
        5. if not then continue on adding it into the map.

        6. return the emprty lst.
        '''
        