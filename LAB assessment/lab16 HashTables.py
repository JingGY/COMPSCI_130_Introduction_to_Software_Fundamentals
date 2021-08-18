#1 2 3 4 5
class SimpleHashTable:
    def __init__(self, size = 7):
        self.__size = size
        self.__slots = []
        for i in range(size):
            self.__slots.append(None)

    def __str__(self):
        return str(self.__slots) #must convert 

    def get_hash_code(self, key):
        hash_code = key % (self.__size)
        return hash_code

    def get_size(self):
        return self.__size

    def __len__(self):
        num = 0
        for i in self.__slots:
            if i != None:
                num += 1
        return num
    
    def get_new_hash_code_linear_probing(self, index):
        new_hash_code = (index + 1) % self.__size 
        return new_hash_code

    def put(self, key):
        if not self.is_full():
            the_index = self.get_hash_code(key)
            while self.__slots[the_index] != None:
                the_index = self.get_new_hash_code_linear_probing(the_index)
            self.__slots[the_index] = key
        else:
            raise IndexError("ERROR: The hash table is full.")

    def is_full(self):
        is_full = True
        for i in self.__slots:
            if i == None:
                is_full = False
                return is_full
        return is_full

    def is_empty(self):
        is_empty = True
        for i in self.__slots:
            if i != None:
                is_empty = False
                return is_empty
            
        return is_empty

    def clear(self):
        for i in range(self.__size):
            self.__slots[i] = None

    def rehashing(self, new_size):
        tem = self.__slots
        self.__slots = []
        for i in range(new_size):
            self.__slots.append(None)
        self.__size = new_size
        for i in tem:
            if i != None:
                self.put(i)


my_hash_table = SimpleHashTable(5)
my_hash_table.put(13)
my_hash_table.put(26)
my_hash_table.put(14)
my_hash_table.put(15)
my_hash_table.rehashing(11)
print(my_hash_table)


#q6
class QuadraticHashTable:
    def __init__(self, size=7):
        self.__size = size
        self.__slots = []
        for i in range(size):
            self.__slots.append(None)

    def __str__(self):
        return str(self.__slots) #must convert 

    def get_hash_code(self, key):
        hash_code = key % (self.__size)
        return hash_code

    def get_size(self):
        return self.__size

    def __len__(self):
        num = 0
        for i in self.__slots:
            if i != None:
                num += 1
        return num

    def put(self, key):
        if not self.is_full():
            the_index = self.get_hash_code(key)
            a_index = self.get_hash_code(key) #must define first
            distance = 1
            while self.__slots[a_index] != None:
                a_index = self.get_new_hash_code_quadratic_probing(the_index, distance)
                distance += 1
            self.__slots[a_index] = key
        else:
            raise IndexError("ERROR: The hash table is full.")

    def is_full(self):
        is_full = True
        for i in self.__slots:
            if i == None:
                is_full = False
                return is_full
        return is_full

    def is_empty(self):
        is_empty = True
        for i in self.__slots:
            if i != None:
                is_empty = False
                return is_empty
            
        return is_empty

    def clear(self):
        for i in range(self.__size):
            self.__slots[i] = None

    def get_new_hash_code_quadratic_probing(self, index, distance):
        new_hash_code = (index + (distance ** 2)) % self.__size
        return new_hash_code

#q7


class DoubleHashTable:
    def __init__(self, size = 7, second_hash_value = 5):
        self.__size = size
        self.__slots = []
        self.__second_hash = second_hash_value
        for i in range(size):
            self.__slots.append(None)

    def __str__(self):
        return str(self.__slots) #must convert 

    def get_hash_code(self, key):
        hash_code = key % (self.__size)
        return hash_code

    def get_size(self):
        return self.__size

    def __len__(self):
        num = 0
        for i in self.__slots:
            if i != None:
                num += 1
        return num

    def put(self, key):
        if not self.is_full():
            the_index = self.get_hash_code(key)
            snew_hash = the_index
            self.__step = 1
            while self.__slots[snew_hash] != None: #must be newhash not the hash, infinit loop
                snew_hash = self.get_new_hash_code_double_hashing(key)
                self.__step += 1
            self.__slots[snew_hash] = key
        else:
            raise IndexError("ERROR: The hash table is full.")


    def get_new_hash_code_double_hashing(self, key):
        step_size = self.__second_hash - (key % self.__second_hash) #must be self.__step
        new_hash_code = (self.get_hash_code(key) + self.__step * step_size) % self.__size
        return new_hash_code

    def is_full(self):
        is_full = True
        for i in self.__slots:
            if i == None:
                is_full = False
                return is_full
        return is_full

    def is_empty(self):
        is_empty = True
        for i in self.__slots:
            if i != None:
                is_empty = False
                return is_empty
            
        return is_empty

    def clear(self):
        for i in range(self.__size):
            self.__slots[i] = None

    def rehashing(self, new_size):
        tem = self.__slots
        self.__slots = []
        for i in range(new_size):
            self.__slots.append(None)
        self.__size = new_size
        for i in tem:
            if i != None:
                self.put(self.get_new_hash_code_linear_probing(i))


#8
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
            
class LinkedListHashTable:
    def __init__(self, size = 7):
        self.__size = size
        self.__slots = []
        for i in range(size):
            self.__slots.append(LinkedList()) #don't put slef

    def get_hash_code(self, key):
        self.code = key % self.__size
        return self.code

    def put(self, key):
        hash_code = self.get_hash_code(key)
        self.__slots[hash_code].add(key)


    def __str__(self):
        message = ""
        for i in self.__slots:
            message += i.__str__() + "\n"
        return message[0:-1]

    def __len__(self):
        count = 0
        for i in self.__slots:
            count += i.size() 
        return count


