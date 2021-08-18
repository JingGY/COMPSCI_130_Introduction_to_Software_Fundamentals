class Node:
    def __init__(self, init_data, init_next_node=None):
        self.__data = init_data
        self.__next = init_next_node

    def get_data(self):
        return self.__data

    def get_next(self):
        return self.__next

    def set_data(self, new_data):
        self.__data = new_data

    def set_next(self, new_next_node):
        self.__next = new_next_node

    def add_after(self, value):
        new_node = Node(value)
        temp = self.get_next()
        self.set_next(new_node)
        self.get_next().set_next(temp)

    def remove_after(self):
        current = self.get_next()
        previous = self
        previous.set_next(current.get_next())
        current.set_next(None)

    def __contains__(self, value):
        is_contains = False
        current = self.get_next()
        if value == self.get_data():
            is_contains = True
        else:
            while current != None:
                if value == current.get_data():
                    is_contains = True
                    return is_contains
                else:
                    current = current.get_next()
        return is_contains

    def __str__(self):
        return str(self.get_data())

    def get_sum(self):
        the_sum = self.get_data()
        current = self.__next
        while current != None:
            the_sum += current.get_data()
            current = current.get_next()
        return the_sum
class LinkedList:
    def __init__(self, head = None):
        self.__head = head

    def add(self, value):
        new_node = Node(value)
        new_node.set_next(self.__head)
        self.__head = new_node
    
    def size(self):
        count = 0
        current = self.__head
        while current != None:
            current = current.get_next()
            count += 1
        return count

    def get_head(self):
        return self.__head

    def clear(self):
        self.__head = None

    def is_empty(self):
        if self.__head == None:
            return True
        else:
            return False

    def __len__(self):
        count = 0
        current = self.__head
        while current != None:
            current = current.get_next()
            count += 1
        return count 

    def __str__(self):
        if self.__len__() != 0:
            message = "["
            current = self.__head
            count = 0
            while current != None:
                message += str(current.get_data())
                count += 1
                if count != self.__len__():
                    message += ", "
                current = current.get_next()
            message += "]"
            return message
        else:
            return "[]"

    def __contains__(self, search_value):
        current = self.__head
        is_find = False
        while current != None:
            if current.get_data() == search_value:
                return True
            else:
                current = current.get_next()

        return is_find

    def __getitem__(self, index):
        current = self.__head
        count = 0
        '''
        while count == index - 1:
            count += 1
            current = current.get_next()
        return current
'''
        for i in range(0, index ):
            current = current.get_next()
        return current.get_data()

    def add_all(self, a_list):
        for i in a_list:
            self.add(i)

    def get_min_odd(self):
        smallest = 999
        current = self.__head 
        while current != None:
            if current.get_data() %2 != 0:
                if current.get_data() < smallest:
                    smallest = current.get_data()
            current = current.get_next()
        return smallest
    
    def reverse(self):
        if self.size() > 1:
            current = self.__head
            after = current.get_next()
            current.set_next(None)
            while after.get_next() != None:
                temp = after.get_next()
                after.set_next(current)
                current = after
                after = temp 
            after.set_next(current)
            #must be there
            self.__head = after
            
    
class SquareNumberIterator:
    def __init__(self, count):
        self.__count = count
        self.__current = 0

    def __next__(self):
        if self.__current < self.__count:
            self.__current += 1
            return (self.__current)**2
        else:
            raise StopIteration
        
#
class SquareNumber:
    def __init__(self, count=5):
        self.__count = count

    def __iter__(self):
        return SquareNumberIterator(self.__count)


for number in SquareNumber(5):
    print(number)

for number in SquareNumber(4):
    print(number)


class LinkedListIterator:
    def __init__(self, head):
        self.__head = head
        self.__current = None

    def __next__(self):
        if self.__current == None:
            self.__current = self.__head
        else:
            self.__current = self.__current.get_next()

        if self.__current == None:
            raise StopIteration
        else:
            return self.__current


