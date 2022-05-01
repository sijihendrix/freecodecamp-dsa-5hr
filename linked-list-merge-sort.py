from linked_list import linkedList

def merge_sort(linked_list):
    """
    Sorts a linked_list in ascending order
    - Recursilevly divide the linked list into sublists containing a single node
    - Repeatedly merge the sublists to produce sorted sublists until one remains 

    Returns a sorted linked list
    """

    if linked_list.size() == 1:
        return linked_list
    elif linked_list.head  is None:
        return linked_list 

    left_half, right_half = split(linked_list)
    left = merge_sort(left_half)
    right = merge_sort(right_half)

    return merge(left, right)


def split(linked_list):
    """
    Divide the onsorted list at midpoint into sublists
    """
    if linked_list == None or linked_list.head is None:
        left_half =  linked_list
        right_half =  None

        return left_half, right_half
    else:
        size = linked_list.size()
        mid = size // 2

        mid_node =  linked_list.node_at_index(mid - 1) 

        left_half =  linked_list
        right_half =  linkedList()
        right_half.head = mid_node.next_node
        mid_node.next_node =  None

    return left_half, right_half


def merge(left, right):
    """
    Merges two linked list sorting by data in the nodes and returns a new, merged list
    
    """

    # create a new linked list that contains nodes from
    # merging left and right
    merged = linkedList()

    # add a fake head that is discarded later 
    merged.add(0)

    # set current head of linked list 
    current = merged.head

    #Obtain head nodes for left and right linked list 
    left_head =  left.head
    right_head = right.head

    #Iterate over left and right until we reach the tailnode of either 

    while left_head or right_head:
        # if the head node of left is None, we're past the tail
        # Add the node from the right to the merged linked list
        if left_head is None:
            current.next_node = right_head
            # call next on right to set loop condition to False
            right_head =  right_head.next_node
        #if head node of rihgt is None we're passed the tail. 
        # add the tail node from left to merged linked lists
        elif right_head is None:
            current.next_node = left_head
            left_head =  left_head.next_node
        else: 
            #not at either tail node
            #obtain node data to perform comparison operations
            left_data = left_head.data
            right_data = right_head.data

            if left_data < right_data:
                current.next_node = left_head
                left_head =  left_head.next_node
            
            else: 
                current.next_node = right_head
                right_head =  right_head.next_node
    
        #move current to next node
        current = current.next_node

    #discard fake head and set first merged node as head
    head = merged.head.next_node
    merged.head = head

    return merged