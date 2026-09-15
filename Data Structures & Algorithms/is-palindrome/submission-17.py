class Solution:
    def isPalindrome(self, s: str) -> bool:

        # s= nolemon,nomelon

        if s is None:
            return False


        new_str = "".join(s).lower()


        left , right = 0 , len(new_str) - 1

        while(left < right):
            while left < right and not new_str[left].isalnum():
                left+=1

            while left < right and not new_str[right].isalnum():
                right-=1

            if new_str[left] != new_str[right]:
                return False


            else:
                left+=1
                right-=1


            

        return True

        
           


        


        '''
        understand 
        1. input - takes a string
        2. output - returns boolean. True if input is palidrome , else False.
        3. edge case - If string 's' is empty. 
        4. core logic - two pointer , isalnum() , split() and .join() , lower()

        plan
        1. Check if the s string is empty , and if it is return False.
        
        2. create a empty string var , and then split() function. 
        
        3. Create a two pointer left and right , where left = 0 and right is the end of the string char.

        3. use a while loop (left < right) , 
             and inside the loop , 
              if left the same as the right , 
                 incrment left and decrement right.

              else , return False

        4. return True after the while loop is over
        '''
        