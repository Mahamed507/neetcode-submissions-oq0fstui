# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:

       

        if list1 is None:
            return list2


        if list2 is None:
            return list1

   


       
        dummy = ListNode()

        curr = dummy

        while list1 and list2:
            if list1.val <= list2.val:

                curr.next = list1
                list1 = list1.next

            else:
                
                curr.next = list2
                list2 = list2.next

            curr = curr.next

        curr.next = list1 or list2
               


        return dummy.next

        '''
        understand
        1. input - takes a head linked list.
        2. output - returns the list that is merged togethor AND is sorted. 
        3. edge case -> if my list1 and list2 is empty. if list1 is just empty or vice versa list2. 

        plan
        1. if list1 and list2 is None return None.
        if list1 is none  , then return list2.
        if list2 is none , then return list1

        2. then create an empty list = ListNode()

        3. use a while loop curr , 
            if list1.val is less or equal then list2.val, 
            list.next = list1.val
             list1 = list1.next

            if list2 <= list1 , then append to my list.
            list.next = list2.val

           list2 = list2.next 

        4. at the end return the list. 
        '''
        