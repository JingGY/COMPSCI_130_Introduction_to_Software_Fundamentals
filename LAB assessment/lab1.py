#10 
word = input('Enter a word: ')

a_dict = dict()
for ele in word:
    a_dict[ele] = ord(ele)

a_dict_key = a_dict.keys()
sorted_key = sorted(a_dict_key)
for key in sorted_key:
    value = a_dict[key]
    print(str(key) + ':' + str(value))

#1
integer = input("Enter an integer: ")
filename = input("Enter a filename: ")
input_file = open(filename, "r")
all_contents = input_file.read()
input_file.close()

contents = all_contents.split()
multiple = [number for number in contents if int(number) % int(integer) == 0]
num = len(multiple)

#num = sum(i for i in all_contents.split() if i%integer == 0)
if num == 1:
    print("There is " + str(num) + " multiple of " +
          str(integer) + " in the '" + filename + "' file.")
else:
    print("There are " + str(num) + " multiples of " +
          str(integer) + " in the '" + filename + "' file.")

#2

filename = input("Enter filename: ")
input_file = open(filename, "r")
all_contents = input_file.read()
input_file.close()
words = all_contents.split()
longest_words = []
len_max = 0
for word in words:
    word = word.lower()
    if (len(word) > len_max):
        longest_words = [word]
        len_max = len(word)
    elif (len(word) == len_max):
        longest_words.append(word)
sort_list = sorted(longest_words)
longest_word = sort_list[-1]
print('The longest word is "' + longest_word + '"')

#3

def get_first3(items):
    first3_list = items[0:3]
    return first3_list

'''print(get_first3([13,42,3,37,9,28]))
'''
#4

def get_sum_positive_even(numbers):
    positve_even_num = [num for num in numbers if num % 2 == 0 and num > 0]
    return sum(positve_even_num)

'''
print (get_sum_positive_even([1,2,3,4,5,-1,-9]))
print (get_sum_positive_even([]))
'''

#5


def get_multiples_of_5(numbers):
    new_list = [num for num in numbers if num % 5 == 0]
    return new_list

#7 unique value


def unique_species(animal_species):
    uniqueValues = sorted(list(set(animal_species.values())))

    return uniqueValues
'''
animal_species={1007:"Meerkat",2091:"Cheetah",13:"Cheetah"}
result=unique_species(animal_species)
print(result)s

'''