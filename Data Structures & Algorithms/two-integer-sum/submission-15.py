class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        map = {}
        values = 0

        if nums == None:
            return []


        for i , n in enumerate(nums):
            values = target - n
           

            if values in map:
                return [map[values] , i]

            else:
                map[n] = i


        

            




        

            




            
        