from operator import le
from turtle import right


def merge_sort(list):
    """
    Sorts a list in ascending order. 
    Returns a new sorted list

    Divide: find the midpoint of the list and divide into sublists 
    Conquer: Recursively sort the sublists created in previous step
    Combile: merge sorted sublists created in previous step
    """

    if len(list) <= 1:
        return list

    left_half, right_half = split(list)
    left = merge_sort(left_half)
    right = merge_sort(right_half)

    return merge(left, right)


def split(list):
    """
    Divide the onsorted list at the middle into sublists
    Returns two sub lists: left and right
    """
    midpoint = len(list)// 2 
    left =  list[:midpoint]
    right = list[midpoint:]

    return left, right

def merge(left, right):
    """
    Merges two lists (arrays), sorting them in the process 
    Returns a new merged list
    """
    l = []
    i = 0
    j = 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            l.append(left[i])
            i += 1
        else: 
            l.append(right[j])
            j += 1 


    while i < len(left):
        l.append(left[i])
        i += 1
    
    while j < len(right):
        l.append(right[j])
        j += 1