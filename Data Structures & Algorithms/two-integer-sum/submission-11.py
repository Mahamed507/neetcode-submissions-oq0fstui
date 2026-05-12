class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prevMp = {} # index : val

        for i , n in enumerate(nums):
            value = target - n
            if value in prevMp:
                return [prevMp[value] , i]
            prevMp[n] = i
        return[]

        
    

        