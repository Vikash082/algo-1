class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


# T: O(n)
def remove_kth_node_from_end(head, k):
    first = second = head
    counter = 1
    # F           S
    # 0->1->2->3->4->5>6
    while counter <= k:
        second = second.next
        counter += 1

    # case for first element ie head
    if second is None:
        first.value = first.next.value
        first.next = first.next.next
        return

    while second.next is not None:
        first = first.next
        second = second.next

    first.next = first.next.next
