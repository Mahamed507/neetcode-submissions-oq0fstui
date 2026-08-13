# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:


        if head is None:
            return None

        prev = None

        curr = head
            
           

        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp

            

        return prev



        '''


        [1] -[2]  -> n
        p    t      c
               
        understand
        1. input - takes a head of a linked list
        2. output - returns the list in a reverse order. 
        3. edge case - if head is none.
        4. core logic - change the reference pointer to an opposite node. 

        plan
        1. if head is none return none.
        2. create var called prev = none and curr = head.
        3. then use a while loop in curr.
        4. inside the looop , 
             temp = curr.next
             curr.next = prev 
             prev = curr 
             curr = prev

        5. return prev
                    
        '''
