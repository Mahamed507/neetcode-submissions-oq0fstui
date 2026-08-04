class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        if nums is None:
            return []

        store = {}
        value = 0

        for i , n in enumerate(nums):
            value = target - n

            if value in store:
                return [store[value] , i]

            store[n] = i 



        return []

        '''
        understanding
        1. input - takes a lst of int.
        2. output - retunrs the index in a array of two elements that equal to the target.
        3. edge case - if my nums(lst) is empty.



        plan
        1. if my nums is empty then return [].
        2. create a empty dict called store.
        3. for loop enumarate  i  , n  ,
             value = target - n 

             then add the 'store' map of the acutal value. 

             if value is in store , return [i , store[i]] 


        4. otherwise return empty lst , []
       
        '''
        