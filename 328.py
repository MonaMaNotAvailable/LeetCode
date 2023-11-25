# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
    
        if not head :
            return head
        odd = head
        even = head.next
        evenHead = even

        #Approach 1: odd's next point to even's next and vice versa
        # while even and even.next:
        #     odd.next = even.next
        #     odd = odd.next
        #     even.next = odd.next
        #     even = even.next

        #Approach 2: both skipping
        while even and even.next:
            odd.next = odd.next.next
            even.next = even.next.next
            odd = odd.next
            even = even.next

        odd.next = evenHead
        return head



        # Approach 3: Use of counter
        # if not head or not head.next:
        #     return head
        
        # even = head
        # odd = head.next

        # dummy = ListNode(-1)
        # dummy.next = even
        # dummy2 = ListNode(-1)
        # dummy2.next = odd

        # node = head
        # counter = 0
        # while node:
        #     if counter > 1:
        #         if counter%2 == 0:
        #             even.next = node
        #             even = even.next
        #         else:
        #             odd.next = node
        #             odd = odd.next

        #     node = node.next
        #     counter +=1
        
        # even.next = dummy2.next
        # odd.next = None

        # return dummy.next