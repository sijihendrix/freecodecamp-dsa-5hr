def binary_search(list, target):
    first = 0
    last = len(list) - 1

    while first <= last:
        midpoint = (first + last) // 2
        if list[midpoint] == target:
            return midpoint
        elif list[midpoint] < target:
            first = midpoint + 1
        else:
            last =  midpoint - 1
    return  None


def verify(index):
    if index is not None:
        print("Target found at: " , index)
    else:
        print("Target not in the list") 



numbers= [0,1,2,3,4,5,6]

result = binary_search(numbers, 5)

verify(result)
