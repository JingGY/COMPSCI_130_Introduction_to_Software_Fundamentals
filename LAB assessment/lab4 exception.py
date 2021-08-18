#quiz before
def mean(data):
    total = 0
    for element in data:
        try:
            total += element
        except:
            pass

    return total / len([num for num in data if not isinstance(num, str)])

print(mean([1,3,'a',4,5]))


#q1
def is_valid_radius(radius):
    try:
        if not isinstance(radius, int) and not isinstance(radius, float):
            raise TypeError()
        if radius <= 0:
            raise ValueError()
        return True
    except TypeError:
        return "ERROR: Invalid radius!"
    except ValueError:
        return "ERROR: Invalid radius!"

#q2 if there is error, then don't need to raise the exception;
    
def is_valid_score(score):
    try:
        if (score >= 0 and score <= 100):
            return True
        if (not isinstance(score, int) and not isinstance(score, float)):
            raise TypeError()
        if (score<0 or score>100):
            raise ValueError()
    except TypeError:
        return "ERROR: Invalid score!"
    except ValueError:
        return "ERROR: Invalid score!"
'''
print(is_valid_score(85.5))
print(is_valid_score(-1))
print(is_valid_score([16, 12]))
print(is_valid_score(123))
print(is_valid_score(0))
print(is_valid_score(100))
print(is_valid_score('sixteen'))
'''

#3


def count_consonants(word):
    try:
        a_list = ["b", "c", "d", "f", "g", "h", "j", "k", "l", "m", "n", "p", "q", "r", "s", "t", "v", "w", "x", "y", "z" ]
        num = 0
        if isinstance(word, str):
            for ele in word:
                if (ele in a_list) :
                    num += 1
            return num
        else:
            raise TypeError()

    except TypeError:
        return("ERROR: Invalid input!")

'''
print(count_consonants('abcdef'))
print(count_consonants('123'))
print(count_consonants(123))
print(count_consonants(''))
print(count_consonants([123]))

print ("question4")
'''
#4
def set_list_element(a_list, index, value) :
    try:
        if not isinstance(index, int):
            raise TypeError()
        else:
            a_list[index]=value

        return list1
    except IndexError:
        print( "ERROR: Invalid index: " + str(index)+".")
    except TypeError:
        print("ERROR: Invalid input.")
    
    finally:
        return a_list

'''

list1 = [1, 2, 3]
set_list_element(list1, 1, 10)
print(list1)

list1 = [1, 2, 3]
set_list_element(list1, 4, 10)
print(list1)

list1 = [1, 2, 3]
set_list_element(list1, 'two', 10)
print(list1)
'''
#5


def get_max(numbers):
    try:
        max = numbers[0]
        for num in numbers:
            if (isinstance(num,int) or isinstance(num,float)):
                if num > max: 
                    max = num
            else:
                raise TypeError()
        return float(max)
    except TypeError:
        return ("ERROR: Invalid number!")


print(get_max([3, -2, 1, 4]))
print(get_max([3, -2, 'two', 4, 'one']))
print(get_max([12, 2.5, 45, 99]))

print("question 6")
def get_sum_even(numbers):
    try:
        sum = 0
        for num in numbers:
            if (isinstance(num, int) or isinstance(num, float)):
                if num % 2 == 0:
                    sum += num
        return sum
    except:
        return 0    

'''
my_list = [1, 2, 3.5, 4, -1, 2]
print(get_sum_even(my_list))
my_list = [1, 2, 3, 4, "two", 2]
print(get_sum_even(my_list))
print(get_sum_even([]))
print(get_sum_even(['NA']))

print("\n")
print('question7')
'''

#7


def get_valid_input():
    number = -1  # default
    
    while not 1 <= number <= 10:
        try:
            user_input = input("Enter a number between 1 and 10 inclusive: ")
            number = float(user_input)
        except:
            number = -1
            
    return float(number)
'''
print("Valid input: {}".format(get_valid_input()))

print("question8")

'''
#q8
def get_volume(radius, height):
    try:
        if (not isinstance(radius, int) or not isinstance(height, int) or not isinstance(radius, float) or not isinstance(height, float)):
            raise TypeError()
        else:
            if radius<0:
                print("ERROR: Radius must be positive.")
            elif (radius<0 and height<0):
                print("ERROR: Height and radius must be positive.")
            elif height<0:
                print("ERROR: Height must be positive.")
            elif (radius==0 or height==0):
                print("ERROR: Not a cylinder.")
            else:
                volumn_clinder=3.1415926535*radius*radius*height
                return volumn_clinder
    except TypeError:
        return ("ERROR: Invalid input.") 




#8
def getvolume(radius, height):
    try:
        if (not isinstance(radius, int) or not isinstance(height, int ) or not isinstance(radius, float) or not isinstance(height, float)):
            raise TypeError()
        else:
            if radius < 0:
                raise TypeError()
            elif (radius < 0 and height < 0):
                print("ERROR: Height and radius must be positive.")
            elif height < 0:
                print("ERROR: Height must be positive.")
            elif (radius == 0 or height == 0):
                print("ERROR: Not a cylinder.")
            else:
                volumn_clinder = 3.1415926535*radius*radius*height
                return volumn_clinder
    except TypeError:
        return ("ERROR: Invalid input.")



def get_volume(radius, height):
    try:
        if (isinstance(radius, (int, float)) and isinstance(height, (int, float))):
            if (radius < 0 and height>0):
                return ("ERROR: Radius must be positive.")
            elif (radius < 0 and height < 0):
                return ("ERROR: Height and radius must be positive.")
            elif (height < 0 and radius>0):
                return ("ERROR: Height must be positive.")
            elif (radius == 0 or height == 0):
                return ("ERROR: Not a cylinder.")
            else:
                volumn_clinder = 3.1415926535*radius*radius*height
                return round(volumn_clinder)
        else:
            raise TypeError()
    except TypeError:
        return ("ERROR: Invalid input.")

'''
print(get_volume(-10, 2))
#ERROR: Radius must be positive.
print(get_volume(10, -2))
#ERROR: Height must be positive.
print(get_volume(-10, -2))
#ERROR: Height and radius must be positive.
print(get_volume(10, 0))
#ERROR: Not a cylinder.
print(get_volume('ten', 2))

print("\n")
print("question9")
'''

#9
def get_maori_word(dictionary, word):
    try:
        m_word = dictionary[word]
        return m_word
    except KeyError:
        message = "ERROR: " +word+" is not available."
        return message


dictionary = {'example': 'tauira', 'house': 'whare', 'apple': 'aporo', 'love': 'aroha', 'food': 'kai',
              'hello': 'kiaora', 'work': 'mana', 'weather': 'huarere', 'greenstone': 'pounamu',
              'red': 'whero', 'orange': 'karaka', 'black': 'mangu'}
'''
print(get_maori_word(dictionary, 'country'))
'''
#10


def get_phone(phones_dictionary, name):
    try:
        if (not isinstance(name, str)):
            raise TypeError()
        elif name != '':
            phone = phones_dictionary[name]
            return phone
        elif name == '':
            raise ValueError()
        

    except TypeError:
        return "ERROR: Invalid input!"
    except KeyError:
        return "ERROR: "+name+" is not available."
 
    except ValueError:
        return "ERROR: Invalid name!"


phones_dictionary = {'Martin': 8202, 'Angela': 6620,
                     'Ann': 4947, 'Damir': 2391, 'Adriana': 7113, 'Andrew': 5654}
'''
print(get_phone(phones_dictionary, 'Ann'))

print(get_phone(phones_dictionary, 'Daniel'))

print(get_phone(phones_dictionary, 123))

print(get_phone(phones_dictionary, ''))
'''
#11

def read_scores(filename):

    try:
        if len(str(filename)) == 0:
            raise ValueError("ERROR: Invalid filename!") #value error 1
        else:
            input_file = open(filename, "r")
            scores = input_file.read().split()
            for num in scores:
                if num.isnumeric() == False:
                    raise ValueError("Invalid value") #value error 2 (don't need to raise it actually)
                else:
                    numbers = [float(score) for score in scores if float(score) >= 0]
                    input_file.close()

            if len(numbers)==0:
                raise ValueError("ERROR: No positive scores in the input file.") #value error 3
    except ValueError as Err:
        print (Err)
    except FileNotFoundError:
        print ("ERROR: The file '" + filename +"' does not exist.")
    except OSError:
        print ("ERROR: Invalid input!")
    else:
        number_of_marks = len(numbers)
        total_marks = sum(numbers)
        print("There are {} score(s).".format(number_of_marks))
        print("The total is {:.2f}.".format(total_marks))
        print("The average is {:.2f}.".format(total_marks/number_of_marks))

'''
read_scores('')
read_scores(123)
read_scores('input_unknown.txt')
read_scores('value.txt')
read_scores('negative.txt')
'''
##lab4 q3


def read_numbers(filename):
    result = []
    try:
        if not isinstance(filename, str):
            raise TypeError("ERROR: Invalid parameter: filename needs to be a string!")
        input_file = open(filename, "r")
        content = input_file.readlines()

        for line in content:
            number = line.split()
            numbers_sum = 0
            for num in number:
                try:
                    '''
                    if not (num.isnumeric() or num.lstrip('-').isnumeric() or num.isdecimal()):
                        raise ValueError()
                    '''
                    number = float(num)
                    numbers_sum += number
                except: 
                    pass
            result.append(numbers_sum)
        input_file.close()
        print(result)

    except TypeError as Err:
        print(Err)
    except FileNotFoundError:
        print("ERROR: The file 'input_unknown.txt' does not exist.")


def read_numbers2(filename):
    result = []
    try:
        if not isinstance(filename, str):
            raise TypeError(
                "ERROR: Invalid parameter: filename needs to be a string!")
        input_file = open(filename, "r")
        content = input_file.readlines()

        for line in content:
            number = line.split()
            numbers_sum = 0
            for num in number:
                try:
                    if not (num.isnumeric() or num.lstrip('-').isnumeric() or num.replace('.', '', 1).isdigit()):
                        raise ValueError()
            
                    number = float(num)
                    numbers_sum += number
                except:
                    pass
            result.append(numbers_sum)
        input_file.close()
        print(result)

    except TypeError as Err:
        print(Err)
    except FileNotFoundError:
        print("ERROR: The file 'input_unknown.txt' does not exist.")


read_numbers2("D:/uni/stage 1/compsci130/lab and practice/week3/eight_numbers.txt")
read_numbers("D:/uni/stage 1/compsci130/lab and practice/week3/with_invalid.txt")
