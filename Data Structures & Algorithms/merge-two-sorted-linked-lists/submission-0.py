# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not (list1 or list2):
            return None
        vals = ListNode()
        curr_1 = list1
        curr_2 = list2

        if curr_1 and curr_2:
            if curr_1.val < curr_2.val:
                vals.val = curr_1.val
                curr_1 = curr_1.next
            else:
                vals.val = curr_2.val
                curr_2 = curr_2.next
        elif curr_1:
            vals.val = curr_1.val
            curr_1 = curr_1.next
        elif curr_2:
            vals.val = curr_2.val
            curr_2 = curr_2.next
        
        curr_val = vals
        while curr_1 and curr_2:
            if curr_1.val < curr_2.val:
                curr_val.next = curr_1
                curr_1 = curr_1.next
                curr_val = curr_val.next
            else:
                curr_val.next = curr_2
                curr_2 = curr_2.next
                curr_val = curr_val.next

        while curr_1:
            curr_val.next = curr_1
            curr_1 = curr_1.next
            curr_val = curr_val.next

        while curr_2:
            curr_val.next = curr_2
            curr_2 = curr_2.next
            curr_val = curr_val.next

        return vals