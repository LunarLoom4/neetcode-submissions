class ListNode:
    def __init__(self, val, nexty = None):
        self.value = val
        self.next = nexty

class LinkedList:

    def __init__(self):
        self.head = ListNode(-1)
        self.tail = self.head

    def get(self, index: int) -> int:
        curr = self.head.next
        i = 0
        while curr != None:
            if i == index:
                return curr.value
            curr = curr.next
            i += 1
        else:
            return -1   # Index out of bounds

    def insertHead(self, val: int) -> None:
        new_node = ListNode(val)            # Step 1: Creates a 'new node' with the given value. Its '.next' pointer is initially set to 'None' (so it is disconnected from the list).
        new_node.next = self.head.next      # Step 2: Points the 'new node' to the current first node, which comes after the 'dummy node'.
        self.head.next = new_node           # Step 3: Updates the pointer of the 'dummy node' to the 'new node', making the 'new node' the first node (or, head node) in the list.
        if new_node.next == None:           # Step 4: If the list was empty, it updates the tail pointer to the new node.
            self.tail = new_node

    def insertTail(self, val: int) -> None:
        new_node = ListNode(val)            # Step 1: Creates a 'new node' with the given value. Its '.next' pointer is initially set to 'None' (so it is disconnected from the list).
        self.tail.next = new_node           # Step 2: Links the current last node to the 'new node'.
        self.tail = self.tail.next          # Step 3: Updates the current tail pointer to the 'new node'. (NOTE: Can also write 'self.tail = new_node' directly.)

    def remove(self, index: int) -> bool:
        i = 0
        curr = self.head                    # Step 1: The pointer 'curr' always lies just behind the 'target node' as 'self.head' will give the dummy node and i = 0 is the actual 'first node' in the list.
        while i < index and curr:           # Step 2: We will keep on incrementing 'i' until 'i' equals 'index' value, and here, 'curr' shall be pointing to the node just before the 'target node'.
            i += 1                          #         (NOTE: For example, if 'index' = 2, then 'curr' shall be pointing at the node having 'index = 1'. This allows us to remove the index at 'index = 2' by equating 'curr.next' to 'curr.next.next'.)
            curr = curr.next                #         (NOTE: 'curr' is also included in the 'while' loop condition as it is possible that the 'curr.next' value at index 'i' is 'null', like, we have to remove value at index = 5, but the list has only until index = 3.)
        
        if curr and curr.next:              # Step 3: To check whether 'curr' or 'curr.next' is null or not. If they are, then False should be returned as there is no node at the asked index. 'curr' takes care for cases where index > len(list) + 1 and 'curr.next' takes care for the edge case when index = len(list) + 1.
            if curr.next == self.tail:      # Step 4: For the edge case where index = len(list), the 'tail node' is shifted to 'curr' as the 'tail node' is going to be removed.
                self.tail = curr
            curr.next = curr.next.next      # Step 5: The pointer from 'curr' is skipped by one node with the node at the 'index' being skipped.
            return True                     # Step 6: When everything's done, we return True to say that removal has happened successfully.
        else:
            return False                    # Step 7: This means that the 'index' is out of bounds, i.e., index > len(list), and so the node could not be removed.

    def getValues(self) -> List[int]:
        curr = self.head.next
        res = []
        while curr:
            res.append(curr.value)
            curr = curr.next

        return res
