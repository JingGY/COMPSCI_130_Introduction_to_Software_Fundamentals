#1
def count_down(n):
    if n == 0:
        print("Go!")
    else:
        print(n)
        count_down(n-1)

count_down(3)

#2
def copy_string(word):

    if len(word) == 1:
        return word[-1]
    else:
        words = word[0]+copy_string(word[1:])
        return words


s = 'hello'
print(copy_string(s))
#3


def reverse_string(word):

    if len(word) == 1:
        return word[0]
    else:
        words = word[-1]+reverse_string(word[0:len(word)-1])
        return words

'''
s = 'hello'
print(reverse_string(s))
'''
#4

def print_between(start, end):
    if start >= end:
        print(end)
    else:
        print(str(start), end = " ") 
        print_between(start+1, end)
'''
print_between(2, 5)
'''
#5
def count_consonants(word):
    string = "bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ"
    if len(word) == 1:
        return 1 if word in string else 0
    else:
        first = 1 if word[0] in string else 0
        rest = count_consonants(word[1:])
        return first + rest
'''
print(count_consonants('This is a Test'))
#print(count_consonants('AEIOU'))
'''
#6
def get_first_lower_case(word):
    if len(word) != 0 and word[0].islower() or len(word) == 1:
        return word[0] if word[0].islower() else None
    else:
        return get_first_lower_case(word[1:])

'''
s = 'WELL done'
print(get_first_lower_case(s))
        
s = 'GREAT'
print(get_first_lower_case(s))
'''
#7 
def get_max_list(numbers):
    if len(numbers) == 1:
        return numbers[0] 
    else:
        return max(numbers[0], get_max_list(numbers[1:])) # extra []



lst = [1, 4, 5, -9]
print(get_max_list(lst))

#8
def get_max_len_list(words):
    if len(words) == 1:
        return len(words[0])
    else:
        return max(len(words[0]), get_max_len_list(words[1:]))

lst = ['This', 'is', 'a', 'test']
print(get_max_len_list(lst))

#9
def no_evens(numbers):
    if len(numbers) == 1 or (numbers[0] % 2 == 0 and len(numbers) != 0): #==1 not 0
        return False if numbers[0]%2 == 0 else True
    else:
        return not numbers[0]%2 == 0 and no_evens(numbers[1:])

print(no_evens([1, 3, 5, 7]))


#10
def evaluate_m(i):

    if i == 1:
        return 1
    else:
        numerator = 1
        denominator = i
        first = numerator/denominator
        return first + evaluate_m(i-1)


print('{} : {}'.format(2, evaluate_m(2)))
print('{} : {:.4}'.format(5, evaluate_m(5)))
