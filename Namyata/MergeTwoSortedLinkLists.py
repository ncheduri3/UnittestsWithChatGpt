import unittest
# You are given the heads of two sorted linked lists list1 and list2.
#
# Merge the two lists in a one sorted list. The list should be made by splicing together the nodes of the first two lists.
#
# Return the head of the merged linked list.



class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def mergeTwoLists(list1, list2):
    head = ListNode()
    current = head
    while list1 and list2:
        if list1.val < list2.val:
            current.next = list1
            list1 = list1.next
        else:
            current.next = list2
            list2 = list2.next
        current = current.next

    current.next = list1 or list2
    return head.next


class MergeTwoListsCorrectedTestCase(unittest.TestCase):
    def test_merge_lists(self):
        # Create the input lists
        # list1: 1 -> 2 -> 4
        list1 = ListNode(1)
        list1.next = ListNode(2)
        list1.next.next = ListNode(4)

        # list2: 1 -> 3 -> 4
        list2 = ListNode(1)
        list2.next = ListNode(3)
        list2.next.next = ListNode(4)

        # Expected merged list: 1 -> 1 -> 2 -> 3 -> 4 -> 4
        expected_output = ListNode(1)
        expected_output.next = ListNode(1)
        expected_output.next.next = ListNode(2)
        expected_output.next.next.next = ListNode(3)
        expected_output.next.next.next.next = ListNode(4)
        expected_output.next.next.next.next.next = ListNode(4)

        finalList = mergeTwoLists(list1, list2)
        fl = []
        while finalList:
            fl.append(finalList.val)
            finalList = finalList.next
        # Call the function and compare the output
        self.assertEqual(fl, [1,1,2,3,4,4])

    def test_empty_lists(self):
        # Empty list1 and list2
        list1 = None
        list2 = None

        # Merged list should be empty as well
        expected_output = None

        self.assertEqual(mergeTwoLists(list1, list2), expected_output)

    def test_one_empty_list(self):
        # list1: 1 -> 2 -> 3
        list1 = ListNode(1)
        list1.next = ListNode(2)
        list1.next.next = ListNode(3)

        # Empty list2
        list2 = None

        # Merged list should be list1 itself
        expected_output = list1

        self.assertEqual(mergeTwoLists(list1, list2), expected_output)

    def test_same_values(self):
        # list1: 1 -> 1 -> 1
        list1 = ListNode(1)
        list1.next = ListNode(1)
        list1.next.next = ListNode(1)

        # list2: 1 -> 1 -> 1
        list2 = ListNode(1)
        list2.next = ListNode(1)
        list2.next.next = ListNode(1)

        # Expected merged list: 1 -> 1 -> 1 -> 1 -> 1 -> 1
        finalList = mergeTwoLists(list1, list2)
        fl = []
        while finalList:
            fl.append(finalList.val)
            finalList = finalList.next
        self.assertEqual(fl, [1,1,1,1,1,1])


if __name__ == '__main__':
    unittest.main()


#can''t compare the address locations of the nodes
#Added the correct test cases.
