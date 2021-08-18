'''
class Triangle: 
    def __init__(self,width, height):
        self.__width = width
        self.__height = height
        self.__area = (self.__width * self.__height) // 2
        
    def get_area(self): 
        return self.__area 
        
    def set_height(self, height):
        self.__height = height
        
    def get_width(self):
        return self.width
    
    def set_height(self, h):
        self.__height = h
        
    def set_weight(self, wedth):
        self.__width = wedth
        
    def __str__(self):
        return "Triangle: " + str(self.__width) +"cm (width) x " + str(self.__height) + "cm (height)"
       
#4
class Cipher:
    def __init__(self, offset, reverse):
        self.__offset = offset
        self.__reverse = reverse
    
     
    def encode(self, word):
        word_acii = [i for i in range(ord("a"), ord("z"))]
        the_word = ""
        for i in word:
            ord_i = ord(i)
            if ord_i + self.__offset < ord('a'):
                the_word += chr(word_acii[ord_i + self.__offset - ord('a')+1])
            elif ord_i + self.__offset > ord('z'):
                the_word += chr(word_acii[ord_i + self.__offset - ord('z')-1])
            else:
                the_word+= chr(ord_i + self.__offset)
            
        if self.__reverse ==  True:
            the_word = the_word[::-1]
        return the_word
        
        
    def decode(self, word):
        word_acii = [i for i in range(ord("a"), ord("z"))]
        the_word = ""
        if self.__reverse ==  True:
            word = word[::-1]
        for i in word:
            ord_i = ord(i)
            if ord_i - self.__offset < ord('a'):
                the_word += chr(word_acii[ord_i - self.__offset - ord('a')-1])
            elif ord_i - self.__offset > ord('z'):
                the_word += chr(word_acii[ord_i - self.__offset - ord('z')+1])
            else:
                the_word+= chr(ord_i - self.__offset)
        
c = Cipher(2, False)
coded_message = c.encode('cat')
print(coded_message)
decoded_message = c.decode(coded_message)
print(decoded_message)
        

#5
class Stack:
    def __init__(self):
        self.__items = []

    def is_empty(self):
        return self.__items == []

    def push(self, item):
        self.__items.append(item)

    def pop(self):
        return self.__items.pop()

    def peek(self):
        return self.__items[len(self.__items) - 1]

    def size(self):
        return len(self.__items)

    def __str__(self):
        return 'Stack: {} <- top of the stack'.format(str(self.__items))    
        
    def slice(self, start, stop, step = 1):
        new_stack = Stack()
        for i in range(start, stop, step):
            new_stack.push(i)
            
  

#7
class Queue:
    def __init__(self):
        self.__items = []

    def is_empty(self):
        return self.__items == []
 
    def enqueue(self, item):
        self.__items.insert(0,item)

    def dequeue(self):
        return self.__items.pop()

    def size(self):
        return len(self.__items)

    def peek(self):
        return self.__items[self.size() - 1]

    def __str__(self):
        return 'Queue: front->{}<- end'.format(str(self.__items[::-1]))  
    
    def  splice(self, second_queue):
        for i in second_queue.__items:
            self.__items.append(i)
        
#8
def create_chain(values_list):
    
    for i in range(len(values_list)):
        if i == 0:
            the_node = Node(values_list[i])
            current = the_node
        else:
            new_node = Node(values_list[i])
            current.set_next(new_node)
            current = current.get_next()
    return the_node
    
def create_chain(elements):
    if len(elements) == 0:
        return None
    for i in range(len(elements)):
        if i == 0:
            head = Node(elements[i])
            current = Node(elements[i])
        else:
            new_node = Node(elements[i])
            current.set_next(new_node)
            current = current.get_next()
    return head
#9
class LinkedList:
    def __init__(self):
        self.__head = None      
    def add(self, item): #add to the beginning of the list
        new_node = Node(item, self.__head)
        self.__head = new_node
    def size(self):
        current = self.__head
        count = 0
        while current != None:
            count = count + 1
            current = current.get_next()
        return count
    def is_empty(self):
        return self.__head == None   
    def __str__(self):
        result = "["
        separator = ""
        current = self.__head
        while current != None:
            result += separator + str(current.get_data())
            separator = ", "
            current = current.get_next()
        result += "]"
        return result
        
    def has_same_elements(self, list2):
        
 
#10

def get_rightmost_data(b_tree):
    if b_tree.get_right() == None:
        return b_tree.get_data()
    else:
        return get_rightmost_data(b_tree.get_right())
        
#11
def print_leaf_nodes(b_tree):
    if b_tree.get_right() == None:
        return b_tree.get_data()
    if b_tree.get_left() == None:
        return b_tree.get_data()
    else:
        print_leaf_nodes(b_tree.get_right())
        print_leaf_nodes(b_tree.get_left())
    '''
#13
def evaluate_f(num):
    if num == 0:
        return 2
    elif num % 2 == 0:
        return evaluate_f(num - 2) + 3
    else:
        return evaluate_g(num) + evaluate_f(num - 1)
        
def evaluate_g(num):
    if num == 1:
        return 3
    elif num % 2 == 0:
        return evaluate_f(num) * evaluate_g(num - 1)
    else:
        return evaluate_g(num-1) - 2

        

#14
class Folder:
    def __init__(self, folder_name, list_of_subfolders, list_of_filenames):
        self.__name = folder_name
        self.__subfolders = list_of_subfolders
        self.__files = list_of_filenames
    def __str__(self):
        return self.__name
    def get_files(self):
        return self.__files
    def get_subfolders(self):
        return self.__subfolders
        
def folder_search(folder, file):

    if file in folder.get_files():
        return folder
    else:
        for i in folder.get_subfolders():
            folder_search(i, file)
        
        
    
b = Folder('Folder_b', [], ['File_0', 'File_1', 'File_2'])
c = Folder('Folder_c', [], ['File_3', 'File_4'])
a = Folder('Folder_a', [b, c], [])
print(folder_search(a, 'File_3'))