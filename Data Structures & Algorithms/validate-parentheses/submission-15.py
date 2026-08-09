class Solution:
    def isValid(self, s: str) -> bool:
  

        stack = []

        map ={  "]":"[" ,
                "}": "{",
                ")":"("  }


        for char in s:
            if char in map:
                if stack and stack[-1] == map[char]:
                    stack.pop()

                else:
                    return False

            else:
                stack.append(char)

        return True if not stack else False



           


            

        '''
        plan
        1. string s is empty return true
        2. create a empty stack
        3. create a empty dict with all the char.
        4. use a for loop and check if s is in dict.
        5. append it into stack
        6. if the opposite of the char ex: ']' then pop the stack, do the rest and return True.
        7. return false
        '''
        