class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        Smap = {}
        Tmap = {}

        for i in range(len(s)):
            Smap[s[i]] = 1 + Smap.get(s[i] , 0)
            Tmap[t[i]] = 1 + Tmap.get(t[i] , 0)

        if Smap == Tmap:
            return True

        return False
        '''
        understand
        1. input - s(string) and t(string)
        2. output - if the same amount of char s and t , then return True otherwise return false.
        3. edge case - if len of s and t or not the same or one or the other is none.

        plan
        1. if len of s and t is not equal then return false.
        2. creeate two maps for s and t. 
        3. for loop, 
            Smap(add the elemtns) + 1
            Tmap(add the element) + 1
        4. if smap and tmap is equal , 
               then return true 

            otherwise return false.
        '''
    