#include <unordered_set>
#include<iostream>
class Solution {
public:
    bool hasCycle(ListNode* head) {
        if (head == nullptr || head->next == nullptr) {
            return false; // No cycle if the list is empty or has only one node
        }

        std::unordered_set<ListNode*> visited; // Hash set to store visited nodes

        ListNode* temp = head;
        while (temp != nullptr) {
            // If the current node is already in the hash set, it indicates a cycle
            if (visited.find(temp) != visited.end()) {
                return true;
            }
            // Mark the current node as visited
            visited.insert(temp);
            temp = temp->next;
        }

        return false; // No cycle found
    }
};
