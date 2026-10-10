class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        if nums == []:
            return []

        heap = []
        map = {}

        for i in nums:
            map[i] = 1 + map.get(i , 0)

           
        for i in map.keys():
            heapq.heappush(heap ,(map[i] , i))

            if len(heap) > k:
                heapq.heappop(heap)


        res = []

        for i in range(k):
            res.append(heapq.heappop(heap)[1])


        return res
        
        '''
        understand
        1. input - takes a nums(list of int) , and k( # of elements to have for your output list , also find the most freq numbers).
        2. output - returns a list of the freq elements. 
        3. edge case - nums is null.

        plan
        1. if nums is None , then return empty list.
        2. create a empty map , create a empty heap.
        3. for loop, 
             add the values in the map. 


        4. for loop for maps , 
              add it inside the heap 


        5. create a empty list
           for i in range(k);
            lst.append(heapq.pop(map))


        6. return lst 
             

        '''
        