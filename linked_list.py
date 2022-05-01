import re


class Node:
    """
    An object for storing a single node on a linked list;
    Models two attributes - data and the link to the next load on the list
    """
    data = None
    next_node = None

    def __init__(self, data) -> None:
        self.data = data

    def __repr__(self) -> str:
        return "<Node data: %s>" % self.data 



class linkedList:
    """""
    Singly linked list
    """""

    def __init__(self):
        self.head = None

    def is_empty(self):
        return self.head == None

    def size(self):
        """""
        Returns number of nodes in the list. takes linear time
        """""
        current = self.head
        count = 0

        while current:
            count += 1
            current = current.next_node
        return count

    
    def add(self, data):
        """
        Adds new node containing data at the head of the list
        Takes 0(1) time
        """

        new_node = Node(data)
        new_node.next_node = self.head
        self.head = new_node

    def search(self, key):
        """
        Search for the first Node containing data that matches the key 
        Return the node or `None`, if not found
        """
        current = self.head
        while current:
            if current.data == key:
                return current
            else:
                current = current.next_node
        return None
    def insert(self, data, index):
        """
        Inserts a new node containing data at index position 
        insertion takes 0(1) time but finding nodes at specific position takes 0(n) time

        There for it takes overall 0(n)
        """

        if index == 0:
            self.add(data)
        elif index > 0:
            new = Node(data)
            position = index
            current = self.head
            while position > 1:
                current = new.next_node
                position -=1
            prev_node = current
            next_node = current.next_node

            prev_node.next_node = new
            new.next_node = next_node

    def remove(self, key):
        """
        Return Node with data that matches the key
        returns the Node or none if they don't exist
        Takes O(n) time.
        """
        current = self.head
        previous = None
        found = False

        while current and not found:
            if current.data == key and current== self.head:
                found = True
                self.head = current.next_node
            elif current.data == key:
                found = True
                previous.next_node = current.next_node
            else: 
                previous = current
                current = current.next_node

        return current 

    def node_at_index(self, index):
        if index == 0:
            return self.head

        else: 
            current = self.head
            position = 0

        while position < index:
            current = current.next_node 
            position += 1

        return current 


    def __repr__(self):
        """
        Return a string representation of the list.
        Takes O(n) time.
        """
        nodes = []
        current = self.head
        while current:
            if current is self.head:
                nodes.append("[Head: %s]" % current.data)
            elif current.next_node is None:
                nodes.append("[Tail: %s]" % current.data)
            else:
                nodes.append("[%s]" % current.data)
            current = current.next_node
        return  '-> '.join(nodes)