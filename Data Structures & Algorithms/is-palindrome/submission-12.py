class Solution:
    def isPalindrome(self, s: str) -> bool:

        update = ""

        for char in s.lower():
            if char.isalnum():
                update = update + char
                update = ''.join(update)

        left = 0
        right = len(update) - 1

        while(left < right):
            if update[left] != update[right]:
                return False
                break

            else:
                left+=1
                right-=1
        return True

            
        