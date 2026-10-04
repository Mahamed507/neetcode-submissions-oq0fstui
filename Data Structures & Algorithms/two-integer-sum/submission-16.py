class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        if nums == None:
            return []

        values = 0
        map = {}

        for i , v in enumerate(nums):
            values = target - v

            if values in map:
                return [map[values] , i] 


            else:
                map[v] = i






        