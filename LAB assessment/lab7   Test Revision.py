#1
def insertion_sort_by_id(data):
    for index in range(1, len(data)):
        item_to_insert = data[index]
        i = index - 1
        while i >= 0 and data[i] > item_to_insert:
            data[i + 1] = data[i]
            i -= 1
        data[i + 1] = item_to_insert
    return data

def insertion_sort(data):
    for index in range(1, len(data)):
        item_to_insert = data[index]
        i = index - 1
        while i >= 0 and data[i][1] < item_to_insert[1]:
            data[i + 1] = data[i]
            i -= 1
        data[i + 1] = item_to_insert


s1 = (7, "Smith")
s2 = (5, "Brown")
s3 = (4, "Chan")
s4 = (2, "Kim")
s5 = (0, "Lin")
s6 = (1, "Singh")
s7 = (3, "Gupta")
students = [s1, s2, s3, s4, s5, s6, s7]
insertion_sort_by_id(students)
for x in students:
    print(x)


#2
def double(my_list):
    for index in range(len(my_list)):
        my_list[index] = my_list[index] * 2
    return (my_list)

'''
numbers = [3, 2, 1]
id_before = id(numbers)
double(numbers)
print(numbers)
id_after = id(numbers)
print(id_before == id_after)  # same reference before and after

my_list = [1, 2, 3]
double(my_list)
print(my_list)
'''

#3
import math


def my_bubble_sort(data):
    for pass_num in range(len(data)-1):
        for i in range(0, len(data)-pass_num-1):
            if data[i] > data[i+1]:
                data[i], data[i+1] = data[i+1], data[i]

    return data

def get_middle_number(numbers):
    numbers = my_bubble_sort(numbers)
    middle_index = math.floor((len(numbers))/2)
    return numbers[middle_index]

'''
numbers1 = [20, 24, 3, 8, 9]  # if sorted [3, 8, 9, 20, 24]
numbers2 = [15, 28, 22, 21]  # if sorted [15, 21, 22, 28]
numbers3 = [18, 9, 8, 5, 12, 25, 4, 3, 7]  # if sorted [3, 4, 5, 7, 8, 9, 12, 18, 25]

print("1.", get_middle_number(numbers1))
print("2.", get_middle_number(numbers2))
print("3.", get_middle_number(numbers3))
'''

#4
import math

def read_file(filename):
    input_file = open(filename, "r")
    all_contents = input_file.read()
    input_file.close()
    contents_list = all_contents.split()
    return contents_list


def get_middle_number_from_file(filename):
    content_list = read_file(filename)
    for i in range(len(content_list)):
        content_list[i] = int(content_list[i])
    number = get_middle_number(content_list)
    return number
'''
print("1.", get_middle_number_from_file('D:/uni/stage 1/compsci130/lab and practice/numbers1.txt'))
print("2.", get_middle_number_from_file('D:/uni/stage 1/compsci130/lab and practice/numbers2.txt'))
print("3.", get_middle_number_from_file('D:/uni/stage 1/compsci130/lab and practice/numbers3.txt'))
'''

#5
import math

def my_bubble_sort2(data):
    try:
        for pass_num in range(len(data)-1):
            for i in range(0, len(data)-pass_num-1):
                if data[i] > data[i+1]:
                    data[i], data[i+1] = data[i+1], data[i]  
    except:
        pass
    return data

def get_middle_number2(numbers):
    numbers = my_bubble_sort2(numbers)
    middle_index = math.floor((len(numbers))/2)
    return numbers[middle_index]


def get_middle_number_from_file(filename):
    try:
        content_list = read_file(filename)
        if len(content_list) == 0:
            raise ValueError("ERROR: " + '"' + filename + '"' + " is empty.")
        new_content_list = []
        for i in range(len(content_list)):
            try:
                num = content_list[i]
                if not num.isdigit():
                    raise ValueError("ERROR: " + '"' + filename +
                                     '"' + " contains an invalid value.")
            except ValueError as Err:
                print(Err)
            else:
                new_content_list.append(int(content_list[i]))

        number = get_middle_number2(new_content_list)
        return number

    except FileNotFoundError:
        return 'ERROR: ' + '"' + filename + '"' + " does not exist."
    except ValueError as Err:
        return Err


print("1.", get_middle_number_from_file(
    'D:/uni/stage 1/compsci130/lab and practice/numbers1.txt'))
print("2.", get_middle_number_from_file(
    'D:/uni/stage 1/compsci130/lab and practice/numbers2.txt'))
print("3.", get_middle_number_from_file(
    'D:/uni/stage 1/compsci130/lab and practice/numbers3.txt'))


#6
def insertion_sort(data):
    for index in range(1, len(data)):
        item_to_insert = data[index]
        i = index - 1
        while i >= 0 and data[i][1] < item_to_insert[1]:
            data[i + 1] = data[i]
            i -= 1
        data[i + 1] = item_to_insert
    return data


def linear_search(student_id, students):
    studetn_list = insertion_sort(students)
    the_name = [name[1] for name in studetn_list if student_id in name]
    if len(the_name) != 0:
        return the_name[0]
    else:
        return None
'''
s1 = (7, "Smith")
s2 = (5, "Brown")
s3 = (4, "Chan")
s4 = (2, "Kim")
s5 = (0, "Lin")
students = [s1, s2, s3, s4, s5]
print(linear_search(0, students))

s1 = (1, "Anderson")
s2 = (2, "Huang")
s3 = (3, "Ng")
s4 = (4, "Roberts")
s5 = (5, "Smith")
s7 = (7, "Zhou")
students = [s1, s2, s3, s4, s5, s7]
print(linear_search(-456, students))
'''


#7

def get_unique_letters(word_a, word_b):
    result = []
    for letter in word_a:
        if letter not in word_b and letter not in result:
            result.append(letter)
    for letter in word_b:
        if letter not in word_a and letter not in result:
            result.append(letter)
    result = sorted(result)
    if len(result) == 0:
        return ""
    else:
        for word in result:
            message = ''.join(sorted(result))
        return message
    #return ''.join(sorted(result))
'''
print(get_unique_letters('hello', 'world'))
print(get_unique_letters('world', 'hello'))
print(get_unique_letters('xa', 'aaxxxaa'))
note: forget empty
'''
#8

def rotate_2(numbers):
    new_list = list(numbers)
    if len(numbers)>1:
        for index in range(len(numbers)):
            new_word = numbers[index]
            new_list[index-2] = new_word
        return new_list
    else:
        return (numbers)

'''
numbers = [19, 51, 39, 90, 94, 96, 8, 15, 51, 79, 40]
print(rotate_2(numbers))
numbers = [1]
result = rotate_2(numbers)
print(result)
numbers = [75, 69, 23, 78, 35, 72, 94, 6, 10, 25]
print(rotate_2(numbers))
numbers = [59, 54, 101, 15, 8, 14, 83, 33, 29, 45, 6, 7, 28, 90]
print(rotate_2(numbers))

note: copy list vs assign to the same address
'''

#9


def get_list_of_odd_maximums(a_list_of_lists):
    list_new = []
    for l in a_list_of_lists:
        odd_list=[num for num in l if num % 2 != 0 ]
        if len(odd_list) >0:
            max_num = odd_list[0]
            for num in odd_list:
                if num > max_num:
                    max_num = num
            list_new.append(max_num)
                    
        else:
            max_num = None
            list_new.append(max_num)

    return list_new
'''
a_list_of_lists = [[4, -4],
                   [-5, -4, -7, 0],
                   [-82],
                   [-5, 5, 3, -2]]
result = get_list_of_odd_maximums(a_list_of_lists)
print("Odd maximums:", result)

a_list_of_lists = [[3, 42, 678, -5, -5],
                   [-4, -2, -33, -29, 0],
                   [51],
                   [4, 6, -4],
                   [-309, -3, -34]]

result = get_list_of_odd_maximums(a_list_of_lists)
print("Odd maximums:", result)

note: wrong place for max_num default value, should be outside loop
'''
#10
import math

def draw_triangle(size = 5):
    try:
        if not isinstance(size, int):
            raise ValueError("ERROR: Invalid input!")
        if size >2:
            if size % 2 == 0:
                 dot_num = 2
            else:
                dot_num = 1 
            for row in range(1, math. ceil(size/2)):
               
                space = (size - dot_num)/2
                for col in range(1, size+1):
                    if col <= space or col > size - space:
                        print(" ", end = "")
                    elif (col == space + 1 or col == size - space):
                        print("X", end = '')
                    else:
                        print('-', end = '')
                
                dot_num += 2
               
                print(" ")
            print("X"*size)
        else:
            raise ValueError("ERROR: The size is too small.")
    except ValueError as Err:
        print(Err)

'''
draw_triangle(10)
draw_triangle(2)
draw_triangle()
draw_triangle("two")
draw_triangle(-8)
'''

#11


def get_position_of_highest(data, index):
    max_letter = data[0]
    for i in range(index+1):
        if max_letter < data[i]:
            max_letter = data[i]
    return data.index(max_letter)


def swaps(data):
    count = 0
    for i in range(len(data)-1, -1, -1):
        index_letter = data[i]
        max_letter_position = get_position_of_highest(data, i)
        max_letter = data[max_letter_position]
        if max_letter > index_letter:
            data[i], data[max_letter_position] = data[max_letter_position], data[i]
            count += 1

    return count

'''
numbers = [0, 4, 2, 7, 5]

print(swaps(numbers))
'''

#12


def insertion_sort_by_id(data):
    for index in range(1, len(data)):
        item_to_insert = data[index]
        i = index - 1
        while i >= 0 and data[i] > item_to_insert:
            data[i + 1] = data[i]
            i -= 1
        data[i + 1] = item_to_insert
    return data


def check_count(value, students):
    count = 0
    max_index = len(students) - 1
    min_index = 0
    students_list = insertion_sort_by_id(students)
    
    while (min_index <= max_index):
        mid_index = math.floor((max_index+min_index)/2)
        if students_list[mid_index][0] == value:
            count += 1
            return count
        elif students_list[mid_index][0] < value:
            min_index = mid_index + 1
            count+=1
        elif students_list[mid_index][0] > value:
            max_index = mid_index - 1
            count+=1
    return -1

'''
s1 = (7, "Smith")
s2 = (5, "Brown")
s3 = (4, "Chan")
s4 = (2, "Kim")
s5 = (0, "Lin")
students = [s1, s2, s3, s4, s5]
print(insertion_sort_by_id(students))
print(check_count(0, students))

s1 = (7, "Smith")
s2 = (5, "Brown")
s3 = (4, "Chan")
s4 = (2, "Kim")
s5 = (0, "Lin")
students = [s1, s2, s3, s4, s5]
print(check_count(7, students))
'''
