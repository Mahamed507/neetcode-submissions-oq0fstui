class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:

        pointer1 = 0

        nums.sort()

        for i in range(1 , len(nums)):
            if nums[pointer1] == nums[i]:
                return True
            else:
                pointer1 +=1
        return False
       




       



        