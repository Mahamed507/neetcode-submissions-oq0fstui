class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        dict1 , dict2  = {}, {}

        if len(s) != len(t):
            return False

        return sorted(s) == sorted(t)




     
      
      
   


        
        