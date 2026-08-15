# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if head is None:
            return False


        curr = head
        map = {}

        while curr.next is not None:
            if curr not in map:
                map[curr] = True
                curr = curr.next

            if curr in map:
                return True

        return False

        '''
        understand
        1. input - the head of a linked list
        2. output - return TRUE if it cycles  , otherwise return False. 
        3. edge case - if head is empty. 


        plan
        1. if head is None , then return False.
        2. create a var called curr = head , and create a empety dict.
        3. use a while (curr.next is not none)

        if curr.val not in dict , then add it into dict. 

        if curr.val in dict , then return True


        4. false


        '''
        