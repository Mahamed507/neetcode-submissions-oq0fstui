class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        # check the length first


        if (len(s) != len(t)):
            return False

        return sorted(s) == sorted(t)
