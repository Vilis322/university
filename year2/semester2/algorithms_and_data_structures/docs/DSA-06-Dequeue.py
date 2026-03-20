class Deque:
    def __init__(self, capacity):
        """
        _summary_

        Args:
            capacity (int): _summary_
        """
        self.capacity = capacity  # TODO: Initialize the deque with a fixed capacity
        self.deque = [None] * capacity  # TODO: Create a fixed-size list
        self.front = -1  # TODO: Set initial front pointer
        self.rear = -1  # TODO: Set initial rear pointer

    def is_empty(self):
        """_summary_"""
        # TODO: Check if the deque is empty

    def is_full(self):
        """_summary_"""
        # TODO: Check if the deque is full

    def insert_front(self, value):
        """_summary_"""
        # TODO: Insert an element at the front of the deque

    def insert_rear(self, value):
        """_summary_"""
        # TODO: Insert an element at the rear of the deque

    def delete_front(self):
        """_summary_"""
        # TODO: Remove and return the front element

    def delete_rear(self):
        """_summary_"""
        # TODO: Remove and return the rear element

    def peek_front(self):
        """_summary_"""
        # TODO: Return the front element without removing it

    def peek_rear(self):
        """_summary_"""
        # TODO: Return the rear element without removing it

    def display(self):
        """_summary_"""
        # TODO: Display all elements in the deque


# Example usage:
dq = Deque(5)
dq.insert_rear(1)
dq.insert_rear(2)
dq.insert_front(0)
dq.display()
dq.delete_front()
dq.display()
dq.insert_front(-1)
dq.insert_rear(3)
dq.display()
