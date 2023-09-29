class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """

        current = ListNode()
        dummy = current
        head1 = list1
        head2 = list2

        while (head1 and head2):
            if head1.val <= head2.val:
                current.next = ListNode(head1.val)
                head1 = head1.next
            else:
                current.next = ListNode(head2.val)
                head2 = head2.next
            current = current.next

        if not head2 and head1:
            current.next = head1

        if not head1 and head2:
            current.next = head2

        return dummy.next
