class Solution:
    def isPalindrome(self, s: str) -> bool:
        '''
        understand
        1. input = > takes a string(sentence)
        2.output => returns true if palidrome , false if not.
        3. edge case => null , numbers
        4. logic => lower() , alpha() , isDigit().


        plan
        1. create empty var , string
        2. update the s into a lower string, then use a for loop
       3. check if its alpha or digit()
       5. then add it into my empty string
       6. return if they both match each other one opposite and foward



        implement
        '''
        strr = ''
        update_s = s.lower()
        
        for c in update_s:
            
            if c.isdigit() or c.isalpha():
                strr = strr + c
    

      

        return strr[::-1] == strr
      

       

