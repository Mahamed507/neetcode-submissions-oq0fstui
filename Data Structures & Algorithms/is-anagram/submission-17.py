class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if len(s) != len(t):
            return False


        if t and s is None:
            return False

        map1 , map2 = {} , {}

        for i in range(len(s)):
            map1[s[i]] = 1 + map1.get(s[i] , 0)
            map2[t[i]] = 1 + map2.get(t[i] , 0)

        if map1 == map2:
            return True

        return False

        

        '''
        plan

        1. if len of t and s is not the same return false
        2. if t and s is none,  return false.
        3. create a empty map1 and map2.
        4. use a for loop , 
           add it into the map1 , and also map2

        5. compare if the values in the map is the same amount , return True otherwise return false.


        '''
        