#1 2
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
            return self.__title + ', ' + self.__code + ' (Available)' 
        
        else:
            return self.__title + ', ' + self.__code + ' (On Loan)'     
        
#3 4
class Memeber:
    def __init__(self, m_id, name):
        self.__id = m_id
        self.__name = name
        self. __on_loan_books_list = []
        
    def get_name(self):
        return self.__name
       
    def get_member_id(self):
        return self.__id
        
    def get_member_id(self):
        return self.__on_loan_books_list
        
    def borrow_book(self, book):
        self.__on_loan_books_list.append(book.get_book_title())
        
    def return_book(self, book):
        i = self.__on_loan_books_list.index(book.get_book_title())
        self.__on_loan_books_list.pop(i)
       
    def __str__(self):
        if len(__on_loan_books_list) == 0:
            return self.__name + '\n' + 'On loan book(s):' + '\n' + "-" 
        else:
            book_list = ''
            for i in self.__on_loan_books_list:
                book_list += i + '\n'
            return self.__name + '\n' + 'On loan book(s):' + '\n' + book_list
         
#5 6
class Record:
    def __init__(self, book, member, date):
        self.__book = book
        self.__member = member
        self.__issue_date = date
        self.__is_on_loan = True
        book.borrow_book()
        member.borrow_book(book)
        
    def get_member_id(self):
        return self.__member.get_member_id()
        
    def get_book_code(self):
        return self.__book.get_book_code()
        
    def get_issue_date(self):
        return self.__issue_date
        
    def is_on_loan(self):
        return self.__is_on_loan
        
    def return_book(self):
        self.__is_on_loan = False
        self.__book.return_book()
        self.__member.return_book(self.__book)
        
    def __str__(self):
        self.__bookMessage = self.__book
        return self.__member.get_name()+', ' +str(self.__bookMessage) + ", issued date=" + str(self.__issue_date)
        
        
#7
class MyLibrary:
    def __init__(self, filename):
        file_read = open(filename, "r")
        content = file_read.read()
        self.__file_list = content.split('\n')
        self.__on_loan_records_list = []
        self.__books_list = []
        for i in self.__file_list:
            self.__books_list.append(Book(i.split(',')[0], i.split(',')[1]))
        print(len(self.__books_list), "books", "loaded.")

    def show_all_books(self):
        for book in self.__file_list:
            print(book)
        
library = MyLibrary('simple_books.txt')
print()
library.show_all_books()
        
        
        