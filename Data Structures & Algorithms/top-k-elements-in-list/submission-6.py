class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        if nums is None:
            return []

        freq = []
        topK = {}

        for i in nums:
            topK[i] = 1 + topK.get(i , 0)

        topK = sorted(topK.items(), key=lambda item: item[1], reverse=True)

        mover = 0

        while mover <  k:
            freq.append(topK[mover][0])


            mover+=1



        return freq


        '''
        understand
        1. input - takes a lst and a k(number of elements that repeats).
        2. output - > returns array of repeating numbers.

        3. edge case - > if lst is empty or k. 


        4. core logic -> dict , for loop , create a empty lst to return later , if statment .


        plan
        1. if nums is [] , then return an empty lst. 
        2. Create a empty lst called freq
        3. create a dict , and call it topK
        4. for loop to iterate throught the list , 

        if nums not in topK: 
            topK[] = 1 + topK(i , 0)
        

        5. sorted(topK.items(), key=lambda item: item[1], reverse=True)



        6. mover = 0
         if mover <= k , 
           then freq.append(topK[mover].values())

           mover+=1

       


     



         

         6. return freq
        
        '''


        