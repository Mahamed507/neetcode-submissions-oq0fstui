class Solution:
    def isPalindrome(self, s: str) -> bool:

        

        if s  == "":
            return True

        left = 0
        right = len(s) - 1

        convert_lower = s.lower()

        join_convert = "".join(convert_lower)

        while(left < right):

            while left < right and not join_convert[left].isalnum():
                left+=1


            while left < right and not join_convert[right].isalnum():
                right-=1

            if join_convert[right] != join_convert[left]:
                return False


            left +=1
            right -=1
          


        return True

        '''
        understand
        1. input -> get a string of sentence.
        2. output - > returns a boolean , True if its a Palidrome. Otherwise return False if not.
        3. edge case -> If string 's' is empty.
        4. core logic -> two pointer , use function called '.lower()'** immutable** , while loop , if statments  , join() , isalnum()


        plan
        1. if s is None , return True.
        2. create a two pointer , left = 0  and right  = len(s) - 1
        3. convert s to lower. Then join them together with no space.
        4. use a while loop (left < right) , 

             if s[left].isalnum() and s[right]... and s[l] == [right],
              increment left 
              decrement right

            else return false 


        5. return true 

          

        '''
        