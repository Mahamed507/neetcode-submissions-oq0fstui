class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        s = defaultdict(list)

        for i in strs:
            sortedS = ''.join(sorted(i))
            s[sortedS].append(i)
        return list(s.values())
        