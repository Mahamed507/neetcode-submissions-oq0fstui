class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        if nums == None:
            return []

        map = {}

        for i , v in enumerate(nums):
            values = target - v
            if values in map:
                return [map[values] , i]
      

            else:
                map[v] = i

        '''
        understand
        1. input - nums(arr of int) , target(int)
        2. output - returns index of the two elements that sum up the target. 
        3. edge case - nums null. 

        plan
        1. if nums is None , thenr return empty array.
        2. create a dict/map(element:index)
        3. for  index and value use enumate , 
             int values = target - v

             if values in map ,
              return [map[i] i]

            else
             map[value] = index



        implement
        '''
        