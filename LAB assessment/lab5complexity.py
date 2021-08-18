'''
def my_function(n):
    count = 4 #return, wile when i = n
    i = 0
    total = 1
    while i<n:
        total += n
        i += 1
        count +=3
    print("number of operation is:" , count)
    return total

result = my_function(3)
print(result)

#2
def rate(n):
    i = n
    count = 4
    total = 0
    while i > 1:
        total += i
        i //= 2
        count = 3
    print("number of operation is:", count)
    return total

#4


def rate(n):
    i = 0
    total = 0
    count=4
    while i < 10:
        j = 0
        count+=4
        while j < n:
            count+=3
            total += j
            j += 1
        i += 1
    print("count is" , count)
    return total

print(rate(1))

#6


def rate(n):
    total = 0
    i = 0
    c = 4+n
    while i < n:
        j = 0
        c += 3
        while j < n:
            c += 3
            total += j
            j += 1
        i += 1

    print("Number of operations:", c)

rate(2)

#7


def rate(n):
    total = 0
    i = 1
    count=4
    while i < n:
        count+=4
        j = 0
        while j < n:
            count+=3
            total += j
            j += 1
        i *= 2
    print("Number of operations:", count)
    return total


rate(2)

#9


def rate(n):
    total = 0
    i = 0
    count=4
    while i < n:
        count+=4
        j = 0
        while j < 2 * n:
            count+=3
            total += j
            j += 1
        i += 1
    
    print("Number of operations:", count)
    return total


rate(2)

#11


def rate(n):
    total = 0
    i = 0
    count=4
    while i < 4:
        count+=4
        j = 0
        while j < i:
            count+=3
            total += j
            j += 1
        i += 1
    print("Number of operations:", count)
    return total


rate(2)



def has_two_adjacent(numbers):
    is_identical=0
    for index in range(len(numbers) - 1):
        if numbers[index] == numbers[index+1]:
            is_identical = 1
    if is_identical==1:
        return True
    else:
        return False


print(has_two_adjacent([1, 2, 2, 1]))
print(has_two_adjacent([1]))
print(has_two_adjacent(['a', 'ab', 'ba', 'a']))




def get_pair_of_largest_numbers(numbers):
    result = [numbers[index] + numbers[index+1]
              for index in range(len(numbers)-1)]
    max_value = result[0]
    
    for index in range(len(result)):
        the_tuple = (numbers[index], numbers[index+1])
        if result[index] > max_value:
            max_value = result[index]
            the_tuple = (numbers[index], numbers[index+1])
    return the_tuple


print(get_pair_of_largest_numbers([10.5, -3, -1, 11]))
print(get_pair_of_largest_numbers([10, 20, 3, 31, 8, 42]))
print(get_pair_of_largest_numbers([10.5, -3]))
'''


def read_numbers(filename):
     read_scores(filename):
    letter_list = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
                    'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    try:
        result = []
        if not isinstance(filename, "str"):
            raise TypeError("ERROR: Invalid parameter: filename needs to be a string!")
        input_file = open(filename, "r")
        content = input_file.readlines()

        for line in content:
            if len(line)==0:
                result=[0]
            words = line.split()
            numbers = []
            for word in words:
                for letter in letter_list:
                    if letter in word:
                        raise ValueError()
                    if letter not in word:
                        number = float(word)
                        numbers.append(number)
                        total_marks = sum(numbers)
                        result.append(total_marks)
            print(result)
    except FileNotFoundError:
        print("ERROR: The file " + filename + ' does not exist.')
    except ValueError:
        for word in words:
                    if letter not in word:
                        number = float(word)
                        numbers.append(number)
                        total_marks = sum(numbers)
                        result.append(total_marks)
            print(result)
    finally:
        input_file.close()

for num in scores:
                for letter in letter_list:
                    if letter in num:
                        raise ValueError("ERROR: The input file contains invalid values.")
            
