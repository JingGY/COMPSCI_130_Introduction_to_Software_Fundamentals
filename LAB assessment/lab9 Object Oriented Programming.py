#1. 2

import re
class Book:
    def __init__(self, code, title):
        self.__code = code
        self.__title = title
        self.__status = True

    def get_book_title(self):
        return self.__title 

    def get_book_code(self):
        return self.__code 
    
    def is_available(self):
        return self.__status 

    def borrow_book(self):
        self.__status = False

    def return_book(self):
        self.__status = True

    def __str__(self):
        if self.__status:
            self.__status_message = "Available"
        else:
            self.__status_message = "On Loan"
        return self.__title + ", " + str(self.__code) +" (" + self.__status_message +")"

'''
b1 = Book("QS12.03.001", "The Lord Of The Rings")
print(b1)
b2 = Book("QK12.04.002", "The Hitchhiker's Guide To The Galaxy")
print(b2)
b2.borrow_book()
print()
print(b2)
'''
#3 4
class Member:
    def __init__(self, memberid, name):
        self.__member_id = memberid
        self.__name= name
        self.__on_loan_books_list = []

    def get_name(self):
        return self.__name

    def get_member_id(self):
        return self.__member_id

    def get_on_loan_books(self):
        return self.__on_loan_books_list

    def borrow_book(self, book):
        book_title = book.get_book_title()
        self.__on_loan_books_list.append(book_title)
        #print(self.__on_loan_books_list)
        
    def return_book(self, book):
        book_title = book.get_book_title()
        index = self.__on_loan_books_list.index(book_title)
        self.__on_loan_books_list.pop(index)

    def __str__(self):
        name = self.get_name()
        book_list = self.__on_loan_books_list
        if len(book_list) == 0:
            book_list = "-"
            message = name + "\n" + "On loan book(s):" + "\n" + str(book_list)
        else:
            message = name + "\n" + "On loan book(s):" 
            for item in book_list:
                message += "\n" + item
        
        return message
'''
m1 = Member(1001, "Michael")
m2 = Member(1002, "Paul")
b1 = Book("QS12.03.001", "The Lord Of The Rings")
b2 = Book("QK12.04.002", "The Hitchhiker's Guide To The Galaxy")
b3 = Book("QS12.02.003", "The Dune Chronicles")
m1.borrow_book(b1)
m1.borrow_book(b2)
m1.borrow_book(b3)
m1.return_book(b1)
print(m1)
print()
print(m2)
'''
#5 6
import re
class Record:
    def __init__(self, book, member, date):
        self.__book = book
        self.__member = member
        self.__issue_date = date
        self.__is_on_loan = True
        self.__member.borrow_book(book)
        self.__book.borrow_book()

    def get_member_id(self):
        self.__member_id = self.__member.get_member_id()
        return self.__member_id

    def get_book_code(self):
        return self.__book.get_book_code()

    def get_issue_date(self):
        return self.__issue_date

    def is_on_loan(self):
        return self.__is_on_loan

    def return_book(self):
        self.__book.return_book()
        self.__member.return_book(self.__book)

    def __str__(self):
        self.__bookMessage = self.__book
        return self.__member.get_name()+', ' +str(self.__bookMessage) + ", issued date=" + str(self.__issue_date)


class MyLibrary:
    def __init__(self, filename):
        try:
            self.__file_read = open(filename, 'r')

        except FileNotFoundError:
            print("ERROR: The file '" + str(filename) + "' does not exist.")
        else:
            self.__file_content = self.__file_read.read()
            self.__file_list = re.split('[,\n]', self.__file_content)

            self.__books_list = [str(Book(self.__file_list[i], self.__file_list[i+1]))
                                 for i in range(0, len(self.__file_list), 2)]
            #print(self.__books_list)

            self.__on_loan_records_list = []
            self.__number = int(len(self.__file_list)/2)
            print(str(self.__number) + " books loaded.")

    def show_all_books(self):
        try:
            for item in self.__books_list:
                print(item)
        except:
            pass #this part didn't do
    
    def find_book(self, code):
        count = -1
        for i in range(0, len(self.__file_list), 2):
            self.__book = Book(self.__file_list[i], self.__file_list[i+1])
            count +=1
            
            if str(code) in self.__books_list[count] and "Available" in self.__books_list[count]:
                return self.__book
            else:
                is_find = 0
        if is_find == 0:
            return None

    def borrow_book(self, book, member, issue_date):
        self.__member = member
        self.__the_book = book
        self.__code = self.__the_book.get_book_code
        
        if self.find_book(self.__the_book.get_book_code) is None:
            self.__bookname = self.__the_book.get_book_title()
            self.__membername = self.__member.get_name()
            self.__message = self.__bookname + " is borrowed by " + self.__membername
            self.__on_loan_records_list.append(self.__message)
            print( self.__on_loan_records_list)
        else:
            print("ERROR: could not issue the book.")
            

library = MyLibrary('D:/uni/stage 1/compsci130/lab and practice/Lab09Files/simple_books.txt')
print()

b1 = library.find_book('QS12.02.003')
m1 = Member(1001, "Michael")
library.borrow_book(b1, m1, "2020-08-12")
print()
print(m1)

input_value = input("Enter your sentence: ")
length = len(input_value)
print("the length of your input is " + str(length))