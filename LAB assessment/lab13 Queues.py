
#1 2 3 4 5 6
class Stack:
    def __init__(self):
        self.__items = []

    def is_empty(self):
        return self.__items == []

    def push(self, item):
        self.__items.append(item)

    def pop(self):
        if self.is_empty():
            raise IndexError("ERROR: The stack is empty!")
        return self.__items.pop()

    def peek(self):
        if self.is_empty():
            raise IndexError("ERROR: The stack is empty!")
        return self.__items[len(self.__items) - 1]

    def __len__(self):
        length = len(self.__items)
        return length

    def clear(self):
        self.__items = []

    def push_list(self, a_list):
        for num in a_list:
            self.push(num)

    def multi_pop(self, number):
        if number > self.__len__():
            return False
        else:
            for i in range(number):
                self.pop()
            return True

    def copy(self):

        copy_stack = Stack()
        copy_stack.push_list(self.__items)
        return copy_stack

    def __eq__(self, other):
        is_same = True
        if isinstance(other, list):  # if a object
            return False
        elif (self.__len__() == other.__len__()):
            for i in range(self.__len__()):
                if self.__items[i] != other.__items[i]:
                    is_same = False

        else:
            is_same = False

        return is_same

    def __str__(self):
        return "Stack: " + str(self.__items)


#1
class Queue:
    def __init__(self):
        self.__items = []

    def is_empty(self):
        return self.__items == []

    def enqueue(self, item):
        self.__items.insert(0, item)

    def dequeue(self):
        if self.is_empty():
            raise IndexError("ERROR: The queue is empty!")
        return self.__items.pop()
        

    def size(self):
        return len(self.__items)

    def peek(self):
        if self.is_empty():
            raise IndexError("ERROR: The queue is empty!")
        return self.__items[len(self.__items)-1]
    
    def __len__(self):
        length = len(self.__items)
        return length
 

    def __str__(self):
     
        return "Queue: " + str(self.__items[::-1])

    def clear(self):
        self.__items = []

    def enqueue_list(self, a_list):
        for num in a_list:
            self.enqueue(num)

    def multi_dequeue(self, number):
        if number > self.__len__():
            return False
        else:
            for i in range(number):
                self.dequeue()
            return True
'''
try:
    q = Queue()
    q.enqueue(2)
    print(q.dequeue())
except IndexError as err:
    print(err)

try:
    q = Queue()
    q.enqueue(2)
    q.enqueue(1)
    print(q.dequeue())
    print(q.dequeue())
    print(q.dequeue())
except IndexError as err:
    print(err)

q = Queue()
q.enqueue(2)
q.enqueue(1)
print(q)
print("The queue contains {} items.".format(len(q)))
q.clear()
print(len(q))

carBrand = Queue()
carlist = ['Audi', 'Honda', 'Toyota', 'Mercedes']
carBrand.enqueue_list(carlist)
print(carBrand)
‘’‘

car_brand = Queue()
car_list = ['Audi', 'Honda', 'Toyota', 'Mercedes']
for elt in car_list:
    car_brand.enqueue(elt)
print(car_brand.multi_dequeue(2))
print(car_brand)
print("The queue contains {} items.".format(len(car_brand)))
'''
def mirror_queue(a_queue):
    new_queue = Queue()

    word_list = []
    while not a_queue.is_empty():
        item = a_queue.dequeue()
        word_list.append(item)
        new_queue.enqueue(item)
    a_stack = Stack()

    for i in word_list:
        a_queue.enqueue(i)
        a_stack.push(i)
    while not a_stack.is_empty():
        item = a_stack.pop()
        a_queue.enqueue(item)

'''
q1 = Queue()
q1.enqueue(1)
q1.enqueue(2)
q1.enqueue(3)
q1.enqueue(4)
q1.enqueue(5)
print(q1)
mirror_queue(q1)
print(q1)
'''

#6
def is_palindrome(word):
    forward_queue = Queue()
    reverse_stack = Stack()

    for char in word:
        forward_queue.enqueue(char)
        reverse_stack.push(char)

    for i in range(len(word)):
        if forward_queue.dequeue() != reverse_stack.pop():
            return False
        
    return True
'''
print(is_palindrome("abcdef"))
'''

#7 8
class CircularQueue:
    def __init__(self, number = 8):
        self.max_queue = number
        self.__items = []
        for i in range(number):
            self.__items.append(None)
        self.__front = 0
        self.__back = len(self.__items) - 1
        self.__count = 0
    

    def is_empty(self):
        if self.__count == 0:
            return True
        else:
            return False

    def __str__(self):
        return str(self.__items) + ", " + "front:" + str(self.__front) + ", back:" +str(self.__back) + ", count:" + str(self.__count)

    def is_full(self):
        if self.__count == self.max_queue:
            return True
        else:
            return False

    def enqueue(self, item):
        if not self.is_full():
            self.__back = (self.__back + 1) % self.max_queue
            self.__items[self.__back] = item
            self.__count += 1
        
        else:
            raise IndexError("ERROR: The queue is full.")

    def dequeue(self):
        if not self.is_empty():
            item = self.__items[self.__front]
            self.__front = (self.__front + 1) % self.max_queue 
            self.__count -= 1
            return item
        else:
            raise IndexError("ERROR: The queue is empty.")
    
    def print_all(self):
        if self.__back > self.__front:
            current_queue = self.__items[self.__front: self.__back +1]
            for i in current_queue:
                print(i, "", end="")
            print(" ")
        elif self.__back < self.__front:
            current_queue1 = self.__items[self.__front: self.__count + 1]
            current_queue2 = self.__items[:self.__back + 1]
            for i in current_queue1:
                print(i, "", end="")
            for i in current_queue2:
                print(i, "", end="")
            print(" ")
        else:
            print(self.__items[self.__back])
            
        




'''
q1 = CircularQueue()
print(q1)
print(q1.is_empty())

try:
    q1 = CircularQueue(4)
    q1.enqueue(1)
    q1.enqueue(2)
    q1.enqueue(3)
    q1.enqueue(4)
    print(q1)
    q1.enqueue(5)
    print(q1)
except IndexError as e:
    print(e)


q1 = CircularQueue(5)
q1.enqueue(1)
q1.enqueue(2)
q1.enqueue(3)
q1.enqueue(4)
q1.enqueue(5)
q1.dequeue()
q1.dequeue()
print(q1)
print()
q1.enqueue(6)
print(q1)
print()
q1.enqueue(7)
print(q1)


try:
    q1 = CircularQueue(3)
    q1.enqueue('a')
    q1.dequeue()
    q1.dequeue()
    q1.dequeue()
except IndexError as e:
    print(e)
'''
q1 = CircularQueue(4)
q1.enqueue(1)
q1.enqueue(2)
q1.enqueue(3)
q1.enqueue(4)
print(q1)
q1.print_all()
print(q1.dequeue())
q1.print_all()


q1 = CircularQueue(4)
q1.enqueue(1)
q1.enqueue(2)
q1.enqueue(3)
q1.enqueue(4)
q1.dequeue()
q1.enqueue(5)
print(q1)
q1.print_all()

q1 = CircularQueue(5)
q1.enqueue(1)
q1.dequeue()
q1.enqueue(2)
print(q1)
q1.print_all()
