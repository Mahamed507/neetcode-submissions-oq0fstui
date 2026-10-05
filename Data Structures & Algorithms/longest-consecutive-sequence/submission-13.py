class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        if nums == []:
            return 0

        set_num = set(nums)

        streak = 0

        for n in set_num:
            if (n-1) not in set_num:
                length = 0
                while (n + 1) in set_num:
                    length = length + 1
                    n+=1

                streak = max(length + 1, streak)

        return streak
        