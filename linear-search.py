from re import L


def linear_search(list, target):
    """
    Returns the index position of the target if found, else returns None
    """
    for i in range(0, len(list)):
        if list[i] == target:
            return i
    return None



def verify(index):
    if index is not None:
        print("Target found at: " , index)
    else:
        print("Target not in the list") 


numbers= [0,3,4,5,5]

result = linear_search(numbers, 5)

verify(result)