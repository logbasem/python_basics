"""
This code will make a list of random numbers and then sort that list.
"""
import random

#a function that takes a minimum, maximum, and amount of numbers, and prints amount of random numbers within range
def list_of_numbers(min, max, amount):
    number_list = []
    for i in range(amount):
        number_list.append(random.randint(min,max))
    return number_list

my_number_list = list_of_numbers(1,100,100)

def sort(given_list):
    loop_counter = 0
    sorted_list = []
    for i, num in enumerate(given_list):
        sorted_list.append(num)
        j = i
        while j-1 != -1:
            if num < sorted_list[j-1]:
                sorted_list[j], sorted_list[j-1] = sorted_list[j-1], sorted_list[j]
            else:
                break
            j = j-1
            loop_counter = loop_counter + 1
    print (loop_counter)
    return sorted_list

print (sort(my_number_list))