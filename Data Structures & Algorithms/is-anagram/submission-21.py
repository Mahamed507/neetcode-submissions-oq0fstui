class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if len(s) != len(t):
            return False


        sMap , tMap = {} , {}

        for i in range(len(s)):
            sMap[s[i]] = 1 + sMap.get(s[i] , 0)
            tMap[t[i]] = 1 + tMap.get(t[i] , 0)

        if tMap == sMap:
            return True

        return False


        '''
        understand
        1. input - s(str) and t(str)
        2. output - return True if anagram otherwise False.
        3. edge case - if s and t are different lengths. 
        4. core logic - Hashmap(dict) , for loop

        plan
        1. if len(s) is not equal to len(t) , then return false
        2. create two maps for s and t.
        3. use a for loop , 
              add the maps (char : freq) for s and t


        4. return if tMap == sMap

        '''
        