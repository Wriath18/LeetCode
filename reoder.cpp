#include <iostream>

// Definition for singly-linked list.
struct ListNode {
    int val;
    ListNode *next;
    ListNode() : val(0), next(nullptr) {}
    ListNode(int x) : val(x), next(nullptr) {}
    ListNode(int x, ListNode *next) : val(x), next(next) {}
};

void printLinkedList(ListNode* head) {
    ListNode* current = head;
    while (current != nullptr) {
        std::cout << current->val << " ";
        current = current->next;
    }
    std::cout << std::endl;
}


void reorderList(ListNode* head) {
    ListNode* arr[15];
    ListNode* last=NULL;
    ListNode* temp = head;
    ListNode* curr = NULL;
    int i=0;
    while (temp != nullptr && i < 15) {
        arr[i++] = temp;
        temp = temp->next;
    }
    int start = 0;
    int end = i-1;
    while(start <= end)
    {
        arr[start]->next = arr[end];
        arr[end]->next = (start == end) ? nullptr : arr[start + 1]; 
        start++;
        end--;
    }

    printLinkedList(head);
}

// Function to print the linked list


int main() {
    // Creating a linked list: 1 -> 2 -> 3 -> 4 -> 5
    ListNode* head = new ListNode(1);
    head->next = new ListNode(2);
    head->next->next = new ListNode(3);
    head->next->next->next = new ListNode(4);
    head->next->next->next->next = new ListNode(5);

    // Printing the linked list
    printLinkedList(head);

    reorderList(head);
    

    // Freeing memory
    ListNode* current = head;
    while (current != nullptr) {
        ListNode* temp = current;
        current = current->next;
        delete temp;
    }

    return 0;
}

