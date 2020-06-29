"""
This code implements the quickSort sorting method.
"""
import random

#a function that takes a minimum, maximum, and amount of numbers, and prints amount of random numbers within range
def list_of_numbers(min, max, amount):
    number_list = []
    for i in range(amount):
        number_list.append(random.randint(min,max))
    return number_list

def partition(a_list, low, high):
    pivot = a_list[high]
    follower = leader = low
    while (leader < high):
        if a_list[leader] <= pivot:
            a_list[leader],a_list[follower] = a_list[follower],a_list[leader]
            follower += 1
        leader += 1
    
    a_list[follower],a_list[high] = a_list[high],a_list[follower]
    return follower

def _quickSort(a_list, low, high):
    if low >= high:
        return
    p = partition(a_list, low, high)
    _quickSort(a_list, low, p-1)
    _quickSort(a_list, p+1, high)

def quickSort(a_list):
    _quickSort(a_list, 0, len(a_list)-1)

my_list = list_of_numbers(1,100,10)

print ("Unsorted List:")
print (my_list)
quickSort(my_list)
print ("Sorted List:")
print (my_list)