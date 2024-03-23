#include <iostream>

struct ListNode {
    int val;
    ListNode *next;
    ListNode() : val(0), next(nullptr) {}
    ListNode(int x) : val(x), next(nullptr) {}
    ListNode(int x, ListNode *next) : val(x), next(next) {}
};

class Solution {
public:
    ListNode* removeZeroSumSublists(ListNode* head) {
        bool yessum = true;
        ListNode* prev = nullptr;
        while(yessum) {
            yessum = false;
            ListNode* temp = head;
            prev = nullptr;
            while (temp != nullptr && temp->next != nullptr) {
                if(temp->val + temp->next->val == 0) {
                    yessum = true;
                    if (prev == nullptr) {
                        head = temp->next->next;
                        delete temp->next;
                        delete temp;
                        temp = head;
                    } else {
                        ListNode* nextNode = temp->next->next;
                        delete temp->next;
                        delete temp;
                        prev->next = nextNode;
                        temp = nextNode;
                    }
                } else {
                    prev = temp;
                    temp = temp->next;
                }
            }
        }
        return head;
    }
};
