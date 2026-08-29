class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        map1 , map2 = {} , {}

        if len(s) != len(t):
            return False


        for char in range(len(s)):
            map1[s[char]] = 1 + map1.get(s[char] , 0)
            map2[t[char]] = 1 + map2.get(t[char] , 0)

        if map1 == map2:
            return True

        return False

        '''
        plan
        1. check if the lengh of s and t. If not return False.
        2. create two maps for s and t. 
        3. then use a for loop , and add it into the map. make sure the values increment as well becuase we could have double letters. 
        4. after appending insdie the two maps then i want to compare if they are the same return true otherwise return false.
      

  
        '''
        

        
        