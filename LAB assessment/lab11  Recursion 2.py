#1 2
class Contact:
    def __init__(self, name, phone_number, email):
        self.__name = name
        self.__phone_number = phone_number
        self.__email = email
        self.__status = True

    def get_name(self):
        return self.__name

    def get_phone_number(self):
        return self.__phone_number

    def get_email(self):
        return self.__email

    def is_active(self):
        return self.__status

    def set_phone_number(self, phone_number):
        self.__phone_number = phone_number

    def set_email(self, email):
        self.__email = email

    def set_active(self, value):
        self.__status = value
    
    def __str__(self):
        if self.__status:
            return (self.__name + " (" + str(self.__phone_number) + "), " + self.__email)
        else:
            return (self.__name + " is an inactive record.")
'''
c1 = Contact("John", "7589943", "john@amail.com")
print(c1.get_name(), c1.get_phone_number(), c1.get_email(), c1.is_active())
c2 = Contact("Kelly", "4344345", "kelly@bmail.com")
print(c2.get_name(), c2.get_phone_number(), c2.get_email(), c2.is_active())

c1 = Contact("John", "7589943", "john@amail.com")
print(c1)
c2 = Contact("Kelly", "4344345", "kelly@bmail.com")
print(c2)
print()
c1.set_phone_number("1234567")
c1.set_email("abc@abc.com")
c2.set_active(False)
print(c1)
print(c2)
'''
#3 4
class PhoneBook:
    def __init__(self):
        self.__phone_book = []

    def load_records(self, filename):
        try:
            self.__input_file = open(filename, "r")
            self.__all_contents = self.__input_file.read()
            self.__input_file.close()
            self.__phone_book += (self.__all_contents.split())
            print(str(len(self.__phone_book)) + " records loaded.")s
            return self.__phone_book

        except FileNotFoundError:
            print("ERROR: The file '" + filename + "' does not exist.")
    
    def show_all_records(self):
        for i in self.__phone_book:
            self.__phone = i.split(",")
            print(Contact(self.__phone[0], self.__phone[1], self.__phone[2]))

    def find_record(self, search_name):
        self.__contact_list = self.__phone_book #is variable

        self.__is_find = None
        for i in self.__contact_list:
            self.__phone = i.split(",")
            if search_name in self.__phone[0]:
                self.__is_find = True
                name = self.__phone[0]
                phone = self.__phone[1]
                email = self.__phone[2]
        if self.__is_find == None:
            return None
        else:
            return Contact(name, phone, email)
       #Contact should write outside the loop
    
    def update_phone(self, search_name, phone_number):
        self.__is_find_update = None
        for i in range(len(self.__phone_book)):
            #print(self.__phone_book[i])
            self.__contact = self.__phone_book[i].split(",")
            #print(self.__contact)
            if search_name == self.__contact[0]:
                self.__is_find_update = True
                self.__phone_book[i] = self.__phone_book[i].replace(self.__contact[1], phone_number) #must = 
                
        if self.__is_find_update == None:
            print("ERROR: " + search_name + " is not found.")
        else:
            print(search_name + "'s contact is updated.")

    def set_active(self, search_name):
        self.__is_find_active = None
        for i in range(len(self.__phone_book)):
            #print(self.__phone_book[i])
            self.__contact = self.__phone_book[i].split(",")
            #print(self.__contact)
            if search_name == self.__contact[0]:
                self.__is_find_active = True
                self.__contact_object = Contact(
                    self.__contact[0], self.__contact[1], self.__contact[2])
                self.__contact_object.set_active(True)
        if self.__is_find_active == None:
            print("ERROR: " + search_name + " is not found.")
        else:
            print(search_name + ' is active from now on.')

    def set_inactive(self, search_name):
        self.__is_find_inactive = None
        for i in range(len(self.__phone_book)):
            #print(self.__phone_book[i])
            self.__contact = self.__phone_book[i].split(",")
            #print(self.__contact)
            if search_name == self.__contact[0]:
                
                self.__is_find_inactive = True

                record = Contact(
                    self.__contact[0], self.__contact[1], self.__contact[2])
          
                record.set_active(False)
                record.is_active()

                
        if self.__is_find_inactive == None:
            print("ERROR: " + search_name + " is not found.")
        else:
            print(search_name + ' is inactive from now on.')

    def show_active_records(self):
        for i in self.__phone_book:
            self.__phone = i.split(",")
            if Contact(self.__phone[0], self.__phone[1], self.__phone[2]).is_active():
                print(Contact(self.__phone[0],
                              self.__phone[1], self.__phone[2]))

    def __len__(self):
        return len(self.__phone_book)


'''
my_phonebook = PhoneBook()
my_phonebook.load_records("D:/uni/stage 1/compsci130/lab and practice/contacts.txt")
print("The phonebook contains {} contacts.".format(len(my_phonebook)))
my_phonebook.show_all_records()

'''
my_phonebook = PhoneBook()
my_phonebook.load_records(
    "D:/uni/stage 1/compsci130/lab and practice/contacts.txt")
my_phonebook.update_phone("John", "1234567")
my_phonebook.update_phone("Paul", "1234567")
print()
my_phonebook.show_all_records()
print()
my_phonebook.set_active("Paul")
my_phonebook.set_inactive("Kelly")
print()
my_phonebook.show_active_records()
print()
my_phonebook.set_active("May")

'''
#5

def get_sum_ascii(word):
    ascii_sum = 0
    if len(word) == 1:
        return ord(word)
    else:
        ascii_sum += ord(word[0]) + get_sum_ascii(word[1:])
        return ascii_sum

print(get_sum_ascii('This is a Test'))
print(get_sum_ascii('T'))

#6


def get_sum_digits(number):
    digits_sum = 0
    number_str = str(number) 
    if len(number_str) == 1:
        return int(number_str)
    else:
        digits_sum = int(number_str[0]) + get_sum_digits(number_str[1:])
        return digits_sum


print(234, ":", get_sum_digits(234))
print(106, ":", get_sum_digits(106))


#7

def get_min_odd(numbers):
    pass

l = [5, 3, 9, 10, 8, 2, 7]

def get_min_odd(l, current_minimum=9999):
    if not l: #if empty
        return current_minimum
    candidate = l.pop()
    if (current_minimum == None or candidate < current_minimum) and candidate % 2 != 0:
        return get_min_odd(l, candidate)
    return get_min_odd(l, current_minimum)


lst = [2]
print(get_min_odd(lst))

#note: determine if emptylist

#8
def get_odds_list(numbers, a_list = None):
    if a_list is None:
        a_list = []
    if not numbers:
        return a_list
    candidate = numbers.pop(0)
    if  (candidate % 2 != 0):
        a_list.append(candidate)
        return get_odds_list(numbers, a_list)

    return get_odds_list(numbers, a_list)

print(get_odds_list([2, 3]))
print(get_odds_list([]))

#q9
def get_merge_list(list_of_lists):
    if len(list_of_lists) == 1:
        return list_of_lists[0]
    else:
        return list_of_lists[0] + get_merge_list(list_of_lists[1:])


print(get_merge_list([[1, 2, 3], [2, 3, 5, 6], [7, 8, 9]]))
print(get_merge_list([[1, 2, 3], [2, 3, 5, 6], [7, 8, 9]]))
print(get_merge_list([[1, 2, 3], [], [7, 8, 9]]))

#q10
def palindrome_filter(sentence):
    new_sentence = ""
    alphabetic = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    if len(sentence) == 1:
        if sentence in alphabetic:
            return sentence
        else:
            return ""
    elif len(sentence) == 0:
        return ""
    else:
        if sentence[0] in alphabetic:
            first = sentence[0].casefold()
        else:
            first = ''
        new_sentence += first + palindrome_filter(sentence[1:])
        return new_sentence

def is_palindrome(sentence):
    if len(sentence) == 2:
        return sentence[0] == sentence[1] 
    elif len(sentence) <= 1:
        return True
    else:
        if sentence[0] == sentence[-1] and is_palindrome(sentence[1:-1]):
            return True
        else:
            return False

print(is_palindrome(palindrome_filter("Able was I ere I saw Elba.")))
print(is_palindrome(palindrome_filter("")))

#q11
# Function to return gcd of a and b


def get_gcd(a, b):
    if a == 0:
        return b
    return get_gcd(b % a, a)

print(get_gcd(100, 70))
print(get_gcd(2, 6))
      
'''
