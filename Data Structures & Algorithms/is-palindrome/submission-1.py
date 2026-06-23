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
        2. for loop  go to opposite
        3. check if its alpha or digit()



        implement
        '''
        strr = ''
        update_s = s.lower()
        
        for c in update_s:
            
            if c.isdigit() or c.isalpha():
                strr = strr + c
    

      

        return strr[::-1] == strr
      

       

