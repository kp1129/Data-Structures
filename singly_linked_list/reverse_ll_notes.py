def reverse_ll(ll):
    """
    Receives a linked list as an input and returns
    a reverse ordered linked list

    Steps:
    1. Each node needs to point at the previous node
    2. Head and tail pointers need to be flipped

    """

    # if LL has more than one node     
    current = ll.head
    previous = None
    while current is not None:
        # store a pointer to the current next value
        next_node = current.get_next()

        # switch current's next pointer to the previous
        current.set_next(previous)

        # increment logic
        previous = current
        current = next_node

    # when the loop finishes, switch head and tail in simultaneous assignment
    # or you can use a temp variable to do the same thing
    ll.head, ll.tail = ll.tail, ll.head 
    # this works even if the LL is empty or has only one node
    # so we don't need extra instructions for those instances

my_ll = LinkedList()
my_ll.add_to_tail(1)
my_ll.add_to_tail(2)
my_ll.add_to_tail(3)
reverse_ll(my_ll)   