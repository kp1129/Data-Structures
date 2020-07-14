"""
Each ListNode holds a reference to its previous node
as well as its next node in the List.
"""
class ListNode:
    def __init__(self, value, prev=None, next=None):
        self.prev = prev
        self.value = value
        self.next = next
            
"""
Our doubly-linked list class. It holds references to 
the list's head and tail nodes.
"""
class DoublyLinkedList:
    def __init__(self, node=None):
        self.head = node
        self.tail = node
        self.length = 1 if node is not None else 0

    def __len__(self):
        return self.length
    
    """
    Wraps the given value in a ListNode and inserts it 
    as the new head of the list. Don't forget to handle 
    the old head node's previous pointer accordingly.
    """
    def add_to_head(self, value):
        self.length += 1
        new_node = ListNode(value)
        if self.head is None and self.tail is None:
            # set head and tail to the new instance
            self.head = new_node
            self.tail = new_node
        new_node.next = self.head
        self.head.prev = new_node
        self.head = new_node
        
    """
    Removes the List's current head node, making the
    current head's next node the new head of the List.
    Returns the value of the removed Node.
    """
    def remove_from_head(self):
        temp = self.head
        if temp.next is not None:
            self.head.next.prev = None
            self.head = temp.next
        else:
            self.head = None
            self.tail = None    
        self.length -= 1
        return temp.value
            
    """
    Wraps the given value in a ListNode and inserts it 
    as the new tail of the list. Don't forget to handle 
    the old tail node's next pointer accordingly.
    """
    def add_to_tail(self, value):
        self.length += 1
        new_node = ListNode(value)
        if self.head is None and self.tail is None:
            # set head and tail to the new instance
            self.head = new_node
            self.tail = new_node
        new_node.prev = self.tail
        self.tail.next = new_node
        self.tail = new_node
            
    """
    Removes the List's current tail node, making the 
    current tail's previous node the new tail of the List.
    Returns the value of the removed Node.
    """
    def remove_from_tail(self):
        # store the value of the tail
        temp = self.tail
        # decrement the length of the dll
        self.length -= 1
        # delete the tail
        if self.tail.prev is not None:
            self.tail.prev.next = None
            self.tail = self.tail.prev
        else:
            self.head = None
            self.tail = None
        return temp.value
            
    """
    Removes the input node from its current spot in the 
    List and inserts it as the new head node of the List.
    """
    def move_to_front(self, node):
        current = self.head
        while node.value != current.value:
            current = current.next
        if current.next is not None:    
            current.next.prev = current.prev.next
            current.prev.next = current.next.prev
        self.head.next = self.head
        self.head = node
        
    """
    Removes the input node from its current spot in the 
    List and inserts it as the new tail node of the List.
    """
    def move_to_end(self, node):
        current = self.tail
        while node.value != current.value:
            current = current.prev
        current.next.prev = current.prev.next
        current.prev.next = current.next.prev
        self.tail.prev = self.tail
        self.tail = node

    """
    Deletes the input node from the List, preserving the 
    order of the other elements of the List.
    """
    def delete(self, node):
        current = self.head
        while node.value != current.value:
            current = current.next
        if current.next is not None:    
            current.next.prev = current.prev.next
            current.prev.next = current.next.prev
        else:
            self.tail = current.prev
            self.tail.next = None

    """
    Finds and returns the maximum value of all the nodes 
    in the List.
    """
    def get_max(self):
        val = self.head.value
        current = self.head
        while current is not None:
            if current.value > val:
                val = current.value
            current = current.next    
        return val