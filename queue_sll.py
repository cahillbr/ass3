# Name:
# OSU Email:
# Course: CS261 - Data Structures
# Assignment:
# Due Date:
# Description:


from SLNode import SLNode


class QueueException(Exception):
    """
    Custom exception to be used by Queue class
    DO NOT CHANGE THIS METHOD IN ANY WAY
    """
    pass


class Queue:
    def __init__(self):
        """
        Initialize new queue with head and tail nodes
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        self._head = None
        self._tail = None

    def __str__(self):
        """
        Return content of queue in human-readable form
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        out = 'QUEUE ['
        if not self.is_empty():
            node = self._head
            out = out + str(node.value)
            node = node.next
            while node:
                out = out + ' -> ' + str(node.value)
                node = node.next
        return out + ']'

    def is_empty(self) -> bool:
        """
        Return True is the queue is empty, False otherwise
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        return self._head is None

    def size(self) -> int:
        """
        Return number of elements currently in the queue
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        node = self._head
        length = 0
        while node:
            length += 1
            node = node.next
        return length

    # -----------------------------------------------------------------------

    def enqueue(self, value: object) -> None:
        """
        TODO: Write this implementation
        """
        # Create a new node
        node = SLNode(value)

        # Check if the queue is empty
        if self.is_empty():
            # Set head and tail to new node
            self._head = node
            self._tail = node

        # Otherwise, add new node to the end of the queue
        else:
            self._tail.nxt = node
            # Update tail to new node
            self._tail = node


    def dequeue(self) -> object:
        """
        TODO: Write this implementation
        """
        # Check if the queue is empty
        if self.is_empty():
            raise QueueException

        # Store the value of the head node
        value = self._head.value

        # Check if there is only one node in the queue
        if self._head == self._tail:
            # Set head and tail to None
            self._head = None
            self._tail = None

        # Otherwise, move head to the next node
        else:
            self._head = self._head.nxt

        # Return the dequeued value
        return value


    def front(self) -> object:
        """
        TODO: Write this implementation
        """
        if self.is_empty():
            raise QueueException

        # Return the value of the head node
        return self._head.value



# ------------------- BASIC TESTING -----------------------------------------


if __name__ == "__main__":

    print("\n# enqueue example 1")
    q = Queue()
    print(q)
    for value in [1, 2, 3, 4, 5]:
        q.enqueue(value)
    print(q)

    print("\n# dequeue example 1")
    q = Queue()
    for value in [1, 2, 3, 4, 5]:
        q.enqueue(value)
    print(q)
    for i in range(6):
        try:
            print(q.dequeue())
        except Exception as e:
            print("No elements in queue", type(e))

    print('\n#front example 1')
    q = Queue()
    print(q)
    for value in ['A', 'B', 'C', 'D']:
        try:
            print(q.front())
        except Exception as e:
            print("No elements in queue", type(e))
        q.enqueue(value)
    print(q)
