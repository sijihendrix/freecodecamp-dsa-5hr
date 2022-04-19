def binary_search(list, target):
    first, last = 0, len(list) - 1

    while first <= last:
        midpoint = first + last // 2
        if list[midpoint] == target:
            return midpoint
        elif list[midpoint] < target:
            first = midpoint + 1
        else:
            last =  midpoint - 1
    return  None
    pass