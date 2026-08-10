class Solution:
    def findMin(self, nums: List[int]) -> int:

        if nums == []:
            return 0

        nums.sort()

        l , r = 0 , len(nums) - 1
        smallest = nums[0]

        while l < r:
            mid = (l + r ) // 2

            if nums[mid] == smallest:
                return smallest

            elif nums[l] < nums[mid]:
                l = l + 1

            else:
                r = r -1

        return smallest



        '''
        understand
        1. input -> takes a list of interger called num.
        2. output -> return the minimum element of the array. Assmuing all elements are already rotated. 
        3. edge case -> if nums array is empty lst.
        4. core logic -> Binary Search.

        plan
        1. check if my nums array is empty.
        2. sort the nums array.
        3. create a two pointer  , can call it left and right. 
        4. create a another var and call it smallest = 0
        5. while loop (left < right)
        6. find the middle , middle = (left + right) // 2
        7. use a if statment , if nums[smallest] == nums[mid] , then return nums[smallest].

        8. if nums[l] < nums[miid] , then increment the left

        else increment the right and add with the midddle 
        '''
        