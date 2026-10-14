class Solution:
    def isPalindrome(self, s: str) -> bool:
        if s == "":
            return False

        left , right = 0 , len(s) - 1

        word = "".join(s)
        convert_word= word.lower()

        while(left < right):
            if (convert_word[left].isalnum() and convert_word[right].isalnum()):
                if (convert_word[left] == convert_word[right]):
                    left+=1
                    right-=1

                else:
                    return False
            elif (convert_word[left].isalnum() != True):
                left+=1
            elif(convert_word[right].isalnum() != True):
                right-=1

                
        return True


        '''
        understand
        1. input - s(string)
        2. output - returns True if palidrome else false.
        3. edge case - if string is null , uppercase or lowercase. 
        4. core logic - use a two pointer. 
        
        plan
        1. check if the string s is null , then return False if it is.
         2. create a two pointer called 'left' and 'right'. 
         3. then convert the word into lowercase and also make sure to  "".join().
         4. Then use a while looop(left < right)
             inside , check if its (check if left and right is either 0-9 or a-z , can use a specific function called isalnum() and if left and right equals the same ) , increment left and decrement right. 
             else, 
             return False



        '''
        
        