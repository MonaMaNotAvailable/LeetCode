# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        # Approach 2: 1*n runtime and use stack(list with pop)
        slow = head
        fast = head
        stack = []
        maxVal = 0

        #find the mid point
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        #add second half to the stack
        while slow:
            stack.append(slow.val)
            slow = slow.next
        
        #find max
        pointer = head
        while len(stack)!=0:
            tempSum = pointer.val + stack.pop()
            maxVal = max(maxVal, tempSum)
            pointer = pointer.next
        
        return maxVal

        # # Approach 2: 2*n runtime and use list & zip
        # #store in a list and find length n
        # temp = []
        # n = 0
        # current = head
        # while current!=None:
        #     temp.append(current.val)
        #     current = current.next
        #     n+=1

        # #go through half of the list to find sums
        # mid_point = n // 2
        # first_half = temp[:mid_point]
        # second_half = list(reversed(temp[mid_point:]))
        # output = [x + y for x, y in zip(first_half, second_half)]
        # print(output)

        # #go through the sums to find the max
        # return(max(output))