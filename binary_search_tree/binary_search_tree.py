"""
Binary search trees are a data structure that enforce an ordering over 
the data they store. That ordering in turn makes it a lot more efficient 
at searching for a particular piece of data in the tree. 

This part of the project comprises two days:
1. Implement the methods `insert`, `contains`, `get_max`, and `for_each`
   on the BSTNode class.
2. Implement the `in_order_print`, `bft_print`, and `dft_print` methods
   on the BSTNode class.
"""
class BSTNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        # check if value is less than self.value
        if value < self.value:
            # if no left child, insert value here
            if self.left is None:
                self.left = BSTNode(value)
            # else repeat the process on left subtree
            else:
                self.left.insert(value)
        # check if value is greater than  (or equal) self.value
        elif value >= self.value:
            # if no right child, insert value here
            if self.right is None:
                self.right = BSTNode(value)
            # else repeat the process on right subtree
            else:
                self.right.insert(value)

    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        if target == self.value:
            return True
        elif target < self.value:
            if self.left is None:
                return False
            else:
                return self.left.contains(target)    
        elif target > self.value:
            if self.right is None:
                return False
            else:
                return self.right.contains(target)    

    # Return the maximum value found in the tree
    def get_max(self):
        # ignore self.left
        # iterate using a loop
        current = self
        max_value = self.value
        while current.right is not None:
            current=current.right
            max_value=current.value
        return max_value


    # Call the function `fn` on the value of each node
    def for_each(self, fn):
        # recursive solution
        fn(self.value)
        if self.right:
            self.right.for_each(fn)
        if self.left:
            self.left.for_each(fn)

    # Part 2 -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self, node):
        # if the current node is None 
        # we know we've reached the end of a recursion
        # (base case) we want to return
        if self is None:
            return

        # check if we can 'move left'
        if self.left is not None:
            self.left.in_order_print(self.left)

        # visit the node by printing its value
        print(self.value)

        # check if we can 'move right'
        if self.right is not None:
            self.right.in_order_print(self.right)  
        

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    

    def bft_print(self, node):
        from queue import Queue
        
        # You should import the queue class from earlier in the
        # week and use that class to implement this method
        # Use a queue to form a "line" 
        # for the nodes to "get in"
        q = Queue()
        # start by placing the root in the queue
        q.enqueue(node)
        
        # while length of queue is greater than 0 
        while q.size > 0:
            # dequeue item from front of queue and print it
            item = q.dequeue()
            print(item.value)
            
            # place current item's left node in queue if not None
            if item.left is not None:
                q.enqueue(item.left)
            # place current item's right node in queue if not None
            if item.right is not None:
                q.enqueue(item.right)


    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    

    def dft_print(self, node):
        from stack import Stack

        # initialize an empty stack
        # push the root node onto the stack
        s = Stack()
        s.push(node)

        # while stack is not empty
        while s.size > 0:
            # pop top item off the stack
            # print that item's value
            item = s.pop()
            print(item.value)

            # if there is a right subtree
            # push right item onto the stack
            if item.right is not None:
                s.push(item.right)

            # if there is a left subtree
            # push left item onto the stack
            if item.left is not None:
                s.push(item.left)

    # Stretch Goals -------------------------
    # Note: Research may be required

    # Print Pre-order recursive DFT
    def pre_order_dft(self, node):
        pass

    # Print Post-order recursive DFT
    def post_order_dft(self, node):
        pass
            