def recursive_binary_search(list, target):
    if len(list) == 0:
        return False
    else:
        midpoint= (len(list)) //2
        if list[midpoint] == target:
            return True
        else:
            if list[midpoint] < target:
                return recursive_binary_search(list[midpoint+1:], target)
            else:
                return recursive_binary_search(list[:midpoint], target)



def verify(index):
    if index is not None:
        print("Target found at: " , index)
    else:
        print("Target not in the list") 


numbers= [0,3,4,5,5]

result = recursive_binary_search(numbers, 7)

verify(result)