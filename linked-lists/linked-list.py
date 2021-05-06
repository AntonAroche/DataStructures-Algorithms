# This class defines a singly-linked list.
class MyLinkedList:
    def __init__(self):
        self.headNode = None

    def get(self, index: int) -> int:
        """
        Get the value of the index-th node in the linked list. If the index is invalid, return -1.
        """
        temp = self.headNode

        for i in range(index):
            if temp.ptr == None:
                return -1

            temp = temp.ptr

        return temp.val

    def addAtHead(self, val: int) -> None:
        """
        Add a node of value val before the first element of the linked list. After the insertion, the new node will be the first node of the linked list.
        """
        node = Node(val, self.headNode)
        self.headNode = node

    def addAtTail(self, val: int) -> None:
        """
        Append a node of value val to the last element of the linked list.
        """
        temp = self.headNode
        while temp.ptr != None:
            temp = temp.ptr

        newNode = Node(val, None)
        temp.setPtr(newNode)

    def addAtIndex(self, index: int, val: int) -> None:
        """
        Add a node of value val before the index-th node in the linked list.
        If index equals to the length of linked list, the node will be appended to the end of linked list.
        If index is greater than the length, the node will not be inserted.
        """
        nextNode = self.headNode

        for i in range(index):
            if nextNode.ptr == None:
                return
            if i = index - 2:
                prevNode = nextNode
            nextNode = nextNode.ptr

    def deleteAtIndex(self, index: int) -> None:
        """
        Delete the index-th node in the linked list, if the index is valid.
        """


class Node:
    def __init__(self, val: int, ptr = None):
        self.val = val
        self.ptr = ptr

    def setPtr(self, ptr):
        self.ptr = ptr

