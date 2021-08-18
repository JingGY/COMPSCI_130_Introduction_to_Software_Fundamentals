
#2
''' not efficent
def bubble_row(data, index):
    i = 0
    while i < index:
        if data[i] > data[i+1]:
            new_larger=data[i]
            new_smaller=data[i+1]
            data[i+1] = new_larger
            data[i] = new_smaller
            i += 1 
        else:
            i += 1
    return data

def bubble_row(data, index):
    for i in range(index-1):
        if data[i] > data[i+1]:
            data[i+1], data[i] = data[i], data[i+1]
    return data
'''

def bubble_row2(data, index):
    for pass_num in range(index):
        for i in range(pass_num):
            if data[i] > data[i+1]:
                data[i], data[i+1] = data[i+1], data[i]

        
letters = ['e', 'd', 'c', 'b', 'a']
def my_bubble_sort(data): 
    for pass_num in range(len(data)-1):
        for i in range(0, len(data)-pass_num-1):
            if data[i] > data[i+1]:
                data[i], data[i+1] = data[i+1], data[i]
                
    return data    
'''
letters = ['m', 'v', 'o', 'd', 'h', 'l', 'y', 's', 'x', 'z']
letters2 = ['m', 'v', 'o', 'd', 'h', 'l', 'y', 's', 'x', 'z']
bubble_row(letters, 4)
print(letters)

bubble_row2(letters2, 4)
print(letters)

#note: forget to use else, so the run time is infinite
'''
#3
def my_bubble_sort(data): 
    for pass_num in range(len(data)-1):
        for i in range(0, len(data)-pass_num-1):
            if data[i] > data[i+1]:
                data[i], data[i+1] = data[i+1], data[i]
                
    return data
'''
letters = ['e', 'd', 'c', 'b', 'a']
my_bubble_sort(letters)
print(letters)


def my_bubble_sort(data): 
    for pass_num in range(len(data)-1, 0, -1):
        for
    '''

#5
def get_position_of_highest(data, index):
    max_letter = data[0]
    for i in range(index+1):
        if max_letter < data[i]:
            max_letter = data[i]
    return data.index(max_letter)

'''
#test
letters = ['e', 'd', 'c', 'b', 'a']
print(get_position_of_highest(letters, 4))

letters = ['g', 'y', 'd', 'h', 'w', 't', 'e',
           'q', 'c', 'x', 'b', 'f', 'u', 'r', 'k', 'm']
print(get_position_of_highest(letters, 2))
#note: data.index isn't max_letter.index
'''

#6


def selection_row(data, index):
    max_letter_index = get_position_of_highest(data, index)
    
    if data[max_letter_index] > data[index]:
        data[index], data[max_letter_index] = data[max_letter_index], data[index]
'''       
letters = ['e', 'd', 'c', 'b', 'a']
selection_row(letters, 4)
print(letters)
   
letters = ['b', 'f', 'u', 'r', 'k']
selection_row(letters, 3)
print(letters)
'''
#q7
def my_selection_sort(data):
    
    for i in range(len(data)-1, -1, -1):
        index_letter = data[i]
        max_letter_position = get_position_of_highest(data, i)
        max_letter = data[max_letter_position]
        if max_letter > index_letter:
            data[i], data[max_letter_position] = data[max_letter_position], data[i]
    
    return data
'''
letters = ['e', 'd', 'c', 'b', 'a']
my_selection_sort(letters)
print(letters)
'''
#9
def shifting(data, index):
    item_to_check = data[index]
    i = index - 1
    while i >= 0 and data[i] > item_to_check:
        data[i+1]=data[i]
        i -=1
    return data
'''
letters = ['a', 'c', 'f', 'b', 'g']
shifting(letters, 3)
print(letters)
#['a', 'c', 'c', 'f', 'g']
letters = ['b', 'c', 'k', 'a', 'z', 'n', 'j', 's']
shifting(letters, 3)
#['b', 'b', 'c', 'k', 'z', 'n', 'j', 's']

print(letters)
note: data[i+1], data[i]= data[i] ,data[i-1] incorrect

'''
#10
def insertion_row(data, index):
    item_to_check = data[index]
    i = index - 1
    while i >= 0 and data[i] > item_to_check:
        data[i+1]=data[i]
        i -=1
    data[i+1] = item_to_check
    return data
'''
letters = ['b', 'c', 'a', 'e', 'f']
#['a', 'b', 'c', 'e', 'f']
insertion_row(letters, 2)
print(letters)

letters = ['h', 't', 'w', 'e', 'q', 'c', 'x']
insertion_row(letters, 3)
print(letters)
#note: data[i+1] is not i-1 or i
'''
#q11
def my_insertion_sort(data):    
    for index in range(1, len(data)):
        item_to_check = data[index]
        i = index - 1
        while i >= 0 and data[i] > item_to_check:
            data[i+1]=data[i]
            i -=1
        data[i+1] = item_to_check
    return data

letters = ['x', 'b', 'f', 'u', 'r', 'k']
my_insertion_sort(letters)
print(letters)

        
        
#q12 Binary Search
import math

def binary_search(numbers, value):
    max_index = len(numbers) - 1
    min_index = 0
    while (min_index <= max_index):
        mid_index = math.floor((max_index+min_index)/2)
        if numbers[mid_index] == value:
            return mid_index
        elif numbers[mid_index] < value:
            min_index = mid_index + 1
        elif numbers[mid_index] > value:
            max_index=mid_index - 1
    return -1

numbers = [10, 15, 20, 27, 41, 69]
print(binary_search(numbers, 69))

numbers = [13, 18, 54, 61, 78, 93]
print(binary_search(numbers, 7))
#note: 1. return mid_index rather than min_index be careful 2. mid_index = (lower + higher)/2 rahter than mins

def binary_search(numbers, value):
    max_index = len(numbers) - 1
    min_index = 0
    while (min_index <= max_index):
        mid_index = math.floor((max_index+min_index)/2)
        if numbers[mid_index] == value:
            return mid_index
        elif numbers[mid_index] < value:
            min_index = mid_index + 1
        elif numbers[mid_index] > value:
            max_index = mid_index - 1
    return -1


numbers = [10, 15, 20, 27, 41, 69]
print(binary_search(numbers, 69))

numbers = [13, 18, 54, 61, 78, 93]
print(binary_search(numbers, 7))

        
    
