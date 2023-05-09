# Name:Brendan Cahill
# OSU Email:cahillbr@oregonstate.edu
# Course: CS261 - Data Structures
# Assignment:3
# Due Date:5/8/23
# Description: Linked List and ADT Implementation


from SLNode import *


class SLLException(Exception):
    """
    Custom exception class to be used by Singly Linked List
    DO NOT CHANGE THIS CLASS IN ANY WAY
    """
    pass


class LinkedList:
    def __init__(self, start_list=None) -> None:
        """
        Initialize new linked list
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        self._head = SLNode(None)

        # populate SLL with initial values (if provided)
        # before using this feature, implement insert_back() method
        if start_list is not None:
            for value in start_list:
                self.insert_back(value)

    def __str__(self) -> str:
        """
        Return content of singly linked list in human-readable form
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        out = 'SLL ['
        node = self._head.next
        while node:
            out += str(node.value)
            if node.next:
                out += ' -> '
            node = node.next
        out += ']'
        return out

    def length(self) -> int:
        """
        Return the length of the linked list
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        length = 0
        node = self._head.next
        while node:
            length += 1
            node = node.next
        return length

    def is_empty(self) -> bool:
        """
        Return True is list is empty, False otherwise
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        return not self._head.next

    # ------------------------------------------------------------------ #

    def insert_front(self, value: object) -> None:
        """
        Insert a new node at the beginning of the list.
        """
        new_node = SLNode(value)
        new_node.next = self._head.next
        self._head.next = new_node

    def insert_back(self, value: object) -> None:
        """
        Insert a new node at the end of the list.
        """
        new_node = SLNode(value)
        current_node = self._head
        while current_node.next:
            current_node = current_node.next
        current_node.next = new_node

    def insert_at_index(self, index: int, value: object) -> None:
        """
        Insert a new node with a specified value at the given index.
        """
        if index < 0:
            raise SLLException("Invalid index")

        new_node = SLNode(value)
        current_node = self._head
        count = 0

        while current_node.next and count < index:
            current_node = current_node.next
            count += 1

        if count == index:
            new_node.next = current_node.next
            current_node.next = new_node
        else:
            raise SLLException("Invalid index")

    def remove_at_index(self, index: int) -> None:
        """
        Remove the node at the specified index.
        """
        if index < 0:
            raise SLLException("Invalid index")

        current_node = self._head
        count = 0

        while current_node.next and count < index:
            current_node = current_node.next
            count += 1

        if current_node.next:
            current_node.next = current_node.next.next
        else:
            raise SLLException("Invalid index")

    def remove(self, value: object) -> bool:
        """
        Remove the first occurrence of the specified value from the list.
        """
        current_node = self._head

        while current_node.next:
            if current_node.next.value == value:
                current_node.next = current_node.next.next
                return True
            current_node = current_node.next

        return False

    def count(self, value: object) -> int:
        """
        Count the number of occurrences of the specified value in the list.
        """
        count = 0
        current_node = self._head.next

        while current_node:
            if current_node.value == value:
                count += 1
            current_node = current_node.next

        return count

    def find(self, value: object) -> bool:
        """
        Check if the specified value is present in the list.
        """
        current_node = self._head.next

        while current_node:
            if current_node.value == value:
                return True
            current_node = current_node.next

        return False

    def slice(self, start_index: int, size: int) -> "LinkedList":
        """
        Return a new linked list containing a slice of the original list.
        """
        if start_index < 0 or size < 0:
            raise SLLException("Invalid start index or size")

        current_node = self._head.next
        count = 0

        while current_node and count < start_index:
            current_node = current_node.next
            count += 1

        if not current_node:
            raise SLLException("Invalid start index")

        sliced_list = LinkedList()
        remaining_size = self.length() - count

        if size > remaining_size:
            raise SLLException("Invalid size")

        while current_node and size > 0:
            sliced_list.insert_back(current_node.value)
            current_node = current_node.next
            size -= 1

        return sliced_list


if __name__ == "__main__":
    lst = LinkedList([1, 2, 3, 4, 5, 6, 7, 8, 9])
    ll_slice = lst.slice(1, 3)
    print("Source:", lst)
    print("Start: 1 Size: 3 :", ll_slice)
    ll_slice.remove_at_index(0)
    print("Removed at index 0 :", ll_slice)