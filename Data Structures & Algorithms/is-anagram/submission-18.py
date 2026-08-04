class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        f = 0
        sec = 0
        
        updatedS = sorted(s)
        updatedT = sorted(t)

        if len(s) != len(t):
            return False


        while(f < len(updatedS) and sec < len(updatedT)):

            if updatedS[f] != updatedT[sec]:
                return False

            else:
                f +=1
                sec +=1

        return True

        