# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:

        #Approach 1: Using fast skipping LinkedList as terminate condition to find the middle ListNode
        if not head.next: return None
        slow, fast = head, head.next.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        slow.next = slow.next.next
        return head
 
        #Approach 2: Brute force with 1.5*O(N) runtime & construct new LinkedList
        # get the length
        # total = 1
        # node = head
        # while node.next != None:
        #     total+=1
        #     node = node.next
        
        # #calculate the middle
        # counter = 0
        # middle = floor(total/2)-1
        # print(middle)
        # node = head

        # #edge case
        # if total ==1:
        #     return None

        # #set up a new LinkedList
        # newHead = ListNode(head.val)
        # newTemp = newHead
        
        # #copy the first half
        # while counter<middle and node.next:
        #     node = node.next
        #     newTemp.next = ListNode(node.val)
        #     newTemp = newTemp.next
        #     counter+=1

        # #reference the later half
        # if node.next and node.next.next:
        #     newTemp.next = node.next.next
        
        # return newHead