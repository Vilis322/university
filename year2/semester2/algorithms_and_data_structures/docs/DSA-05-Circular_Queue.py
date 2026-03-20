class CircularQueue:
    def __init__(self, capacity):
        """
        _summary_

        Args:
            capacity (int): _description_
        """
        self.capacity = capacity  # TODO: Initialize the queue
        self.queue = [None] * capacity  # TODO: Create a fixed-size list
        self.front = -1  # TODO: Set initial front pointer
        self.rear = -1  # TODO: Set initial rear pointer

    def is_empty(self):
        """_summary_"""
        # TODO: Check if the queue is empty

    def is_full(self):
        """_summary_"""
        # TODO: Check if the queue is full

    def enqueue(self, value):
        """_summary_"""
        # TODO: Implement enqueue operation

    def dequeue(self):
        """_summary_"""
        # TODO: Implement dequeue operation

    def peek(self):
        """_summary_"""
        # TODO: Return the front element without removing it

    def display(self):
        """_summary_"""
        # TODO: Display all elements in the queue


# Example usage:
cq = CircularQueue(5)
cq.enqueue(1)
cq.enqueue(2)
cq.enqueue(3)
cq.enqueue(4)
cq.enqueue(5)
cq.display()
cq.dequeue()
cq.display()
cq.enqueue(6)
cq.display()
