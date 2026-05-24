class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        map = {}
        heap = []

        for i in range(len(nums)):
            map[nums[i]] = 1 + map.get(nums[i] , 0)


        for num , freq in map.items():
            heapq.heappush(heap , (freq , num))

            if len(heap) > k:
                heapq.heappop(heap)

        res = []

        for i in range(k):
            res.append(heapq.heappop(heap)[1])

        return res

       

        
        

        

        