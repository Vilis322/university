# Replace # TODO: with your code

class Node:
    def __init__(self, data):
        """_summary_

        Args:
            data (_type_): _description_
        """
        # TODO:


class CircularLinkedList:
    def __init__(self):
        """_summary_
        """
        self.head = None

    # create the linked list: 90->80->60->50
    def create_mock_linked_list(self):
        """_summary_
        """
        node1 = Node(90)
        node2 = Node(80)
        node3 = Node(60)
        node4 = Node(50)

        # TODO:

    # display circular linked list A->B->C in format: A->B->C->A
    def display(self):
        """_summary_
        """
        current = self.head
        while current:
            print(f"{current.data}", end="->")
            current = current.next
        print(None)

    # method to append a node
    def append(self, data):
        # TODO:

    # insert node to linked list
    def insert_node(self, data, position: int):
        """_summary_

        Args:
            data (_type_): _description_
            position (_type_): _description_
        """
        # TODO:

    # method to delete node at the given position
    def delete_node(self, position: int):
        """_summary_

        Args:
            position (int): _description_
        """


# Start of the script
linked_list = CircularLinkedList()

# create the initial linked list
linked_list.create_mock_linked_list()

# print the updated linked list
linked_list.display()
