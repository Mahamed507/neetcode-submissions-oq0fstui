class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        if nums == None:
            return []

        map = {}

        freq = [ [] for i in range(len(nums) + 1)]

        for i in nums:
            map[i] = 1 + map.get(i , 0)

        
        for i , v in map.items():
            freq[v].append(i)

        
        final  = []
 

        for i in range(len(freq) -1 , 0 , -1):
            for num in freq[i]:
                final.append(num)
                if len(final) == k:
                    return final
                
         

            
               
            

    




        '''
        understand

        1. input - nums(arr) and k(int)
        2. output - returns array find the most freq based on k. 
        3. edge case - if nums is None.
        core logic: use bucket sort , heap 
        plan
        1. check if nums is None , return [].
        2. create a empty hashmap .
        3. create an array and use a for loop to keep track f the index as how many freq.
        4. use a for loop,
             add the map to keep track of the freq.

        5. for loop k,v in map.items() , 
                append the array(the index is based on the v)
        6. create another list again to return later. 
          for loop using array from step 5 and start from last to the end by one time. ,
           if len of new array is < k 
              continue 

        7. return new array.
              
               
        '''
        