class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:

        counter = 0
        max_count = 0

        for n in nums:
            if n == 1:
                counter+=1
                max_count = max(max_count , counter)
            if n == 0:
               
                counter = 0
                
        return max_count






        