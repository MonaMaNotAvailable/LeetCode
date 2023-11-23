/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */
class Solution {
public:
    ListNode* reverseList(ListNode* head) {
        //iterative
        ListNode *nextNode, *prevNode = NULL;
        while (head) {
            nextNode = head->next;
            head->next = prevNode;
            prevNode = head;
            head = nextNode;
            }
        return prevNode;

        //recursive
        // if(head == NULL || head->next == NULL) return head;
        // ListNode* prev = NULL;
        // ListNode* sublist = reverseList(head->next);
        // head->next->next = head;
        // head->next=prev;
        // return sublist;
    }
};