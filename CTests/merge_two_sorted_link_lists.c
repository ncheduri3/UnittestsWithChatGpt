#include <stdio.h>
#include <stdlib.h>

struct ListNode {
    int val;
    struct ListNode* next;
};

struct ListNode* mergeTwoLists(struct ListNode* list1, struct ListNode* list2) {
    // Check for empty lists
    if (list1 == NULL)
        return list2;
    if (list2 == NULL)
        return list1;

    struct ListNode* mergedList = NULL;
    struct ListNode* current = NULL;

    // Set the head of the merged list
    if (list1->val <= list2->val) {
        mergedList = list1;
        list1 = list1->next;
    } else {
        mergedList = list2;
        list2 = list2->next;
    }
    current = mergedList;

    // Merge the remaining nodes
    while (list1 != NULL && list2 != NULL) {
        if (list1->val <= list2->val) {
            current->next = list1;
            list1 = list1->next;
        } else {
            current->next = list2;
            list2 = list2->next;
        }
        current = current->next;
    }

    // Append any remaining nodes from list1 or list2
    if (list1 != NULL)
        current->next = list1;
    if (list2 != NULL)
        current->next = list2;

    return mergedList;
}

// Function to create a new node
struct ListNode* createNode(int value) {
    struct ListNode* newNode = (struct ListNode*)malloc(sizeof(struct ListNode));
    newNode->val = value;
    newNode->next = NULL;
    return newNode;
}

// Function to print the linked list
void printListAndCheck(struct ListNode* head, struct ListNode* expected) {
    struct ListNode* current = head;
    struct ListNode* expected_current = expected;
    while (current != NULL && expected_current != NULL) {
        if (current->val != expected_current->val) {
            printf("test case failed");
            return;
        }
        current = current->next;
    }
    printf("\n");
    printf("Test case passed");
}

test_case_one() {
    // Create the first sorted linked list: 1 -> 3 -> 5
    struct ListNode* list1 = createNode(1);
    list1->next = createNode(1);
    list1->next->next = createNode(1);

    // Create the second sorted linked list: 2 -> 4 -> 6
    struct ListNode* list2 = createNode(1);
    list2->next = createNode(1);
    list2->next->next = createNode(1);

    // Create the second sorted linked list: 2 -> 4 -> 6
    struct ListNode* expected = createNode(1);
    expected->next = createNode(1);
    expected->next->next = createNode(1);
    expected->next->next->next = createNode(1);
    expected->next->next->next->next = createNode(1);
    expected->next->next->next->next->next = createNode(1);

    // Merge the two sorted linked lists
    struct ListNode* mergedList = mergeTwoLists(list1, list2);
    printListAndCheck(mergedList, expected);

        // Free memory
    while (mergedList != NULL) {
        struct ListNode* temp = mergedList;
        mergedList = mergedList->next;
        free(temp);
    }

}

int main() {
    test_case_one();


    return 0;
}
