class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if nums is None:
            return 0

        longest = 0
        
        
      
        set_nums = set(nums)

        for n in set_nums:
            if (n-1) not in set_nums:
                curr = 1
                length = 1
                while (n + curr) in set_nums:
                    length +=1
                    curr+=1

                longest = max(longest , length)

        

          
    
        return longest

          
            
        

        '''
        1. check if nums is empty , return 0 
        2. create var ' longest ' and set it to 0
        3. convert nums array into set. 
        4. use a for loop 'n' to iterate through nums.
        5. if nums[n - 1] not in sets , 
               length = 0 
               while (n + 1) in sets,
               length+=1
            longest = max(longest , length)

        6. return longest
        '''
        