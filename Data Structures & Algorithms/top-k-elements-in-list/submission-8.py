class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        map = {}

        for freq in nums:
            map[freq] = 1 + map.get(freq, 0)


        heap = []

        for n in map.keys():
            heapq.heappush(heap , (map[n] , n))

            if len(heap) > k:
                heapq.heappop(heap)


        res = []

        for i in range(k):
            res.append(heapq.heappop(heap)[1])

        return res
        