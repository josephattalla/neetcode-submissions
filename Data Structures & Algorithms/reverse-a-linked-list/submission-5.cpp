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
    ListNode* reverseList(ListNode* node, ListNode* prev) {
        if (!node) return prev;
        ListNode* nxt = node->next;
        node->next = prev;
        return reverseList(nxt, node);
    }
    ListNode* reverseList(ListNode* head) {
        return reverseList(head, nullptr);
    }
};
