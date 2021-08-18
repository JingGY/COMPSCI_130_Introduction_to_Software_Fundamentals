#q1
def highest_value_word(word1, word2, ordinal_position=1):
    index_position = ordinal_position - 1
    if ordinal_position == len(word1) and ordinal_position == len(word1) == len(word2) and ord(word1[index_position]) == ord(word2[index_position]):
        return 0
    elif  ordinal_position == len(word1) and len(word1) < len(word2):
        return  str(ordinal_position + 1)
    elif ordinal_position == len(word1) and len(word1) > len(word2):
        return '-' + str(ordinal_position )
    if ord(word1[index_position]) > ord(word2[index_position]):
        return '-' + str(ordinal_position)
    elif ord(word1[index_position]) < ord(word2[index_position]):
        return str(ordinal_position)
    else:
        return highest_value_word(word1, word2, ordinal_position + 1)

#q2
class UndoRedo:
    def __init__(self):
        self.__back = Stack()
        self.__forward = Stack()
        self.__current = None
    
    def get_prev(self):
        if self.__back.size() != 0:
            value = self.__back.pop()
            self.__forward.push(self.__current)
            self.__current = value
            return value
        else:
            return None
        
    def get_next(self):
        if self.__forward.size() != 0:
            self.__back.push(self.__current)
            value = self.__forward.pop()
            self.__current = value
            return value
        else:
            return None

    def add_item(self, data):
        self.__back.push(self.__current)
        self.__current = data
        for i in range(0, self.__forward.size()):
            self.__forward.pop()


def selection_order(items, interval):
    new_q = Queue()
    new_list = []
    for i in items:
        new_q.enqueue(i)
    count = 0
    while not new_q.is_empty():
        count += 1
        value = new_q.dequeue()
        if count % interval == 0:
            new_list.append(value)
        else:
            new_q.enqueue(value)
            
    return new_list

class QueueAsLinkedList:
    def __init__(self):
        self.__head = None
        self.__tail = None
        self.__count = 0

    def size(self):
        return self.__count

    def enqueue(self, item):
        self.__count += 1
        if self.__head == None:
            self.__head = Node(item)
        else:
            current = self.__head 
            while current.get_next() != None:
                current = current.get_next()
            current.set_next(Node(item))
            self.__tail = current
            
    def dequeue(self):
        if self.__head != None:
            value = self.__head 
            next_value = self.__head.get_next()
            self.__head = next_value
            self.__count -= 1
            return value
        else:
            return None

    def peek(self):
        if self.__head != None:
            return self.__head.get_data()
        else:
            return None

    def is_empty(self):
        if self.__count == 0:
            return True
        else:
            return False



def hash_string_weighted_folding(string_to_hash, modulus):
    a_list = []
    for i in range(0, len(string_to_hash), 4):
        if i+4 < len(string_to_hash):
            new_string = string_to_hash[i:i+4]
        else:
            new_string = string_to_hash[i:]
        a_list.append(new_string)
    hash_sum = 0
    
    for i in a_list:
        count = 0
        for j in i:
            hash_sum += ord(j) * (256 ** count)
            count += 1
    hash_code = hash_sum % modulus
    return hash_code


def hash_string_weighted_folding(string_to_hash, modulus):
    a_list = []
    for i in range(0, len(string_to_hash), 4):
        if i+4 < len(string_to_hash):
            new_string = string_to_hash[i:i+4]
        else:
            new_string = string_to_hash[i:]
        a_list.append(new_string)
    hash_sum = 0
    
    for i in a_list:
        count = 0
        for j in i:
            hash_sum += ord(j) * (256 ** count)
            count += 1
    hash_code = hash_sum % modulus
    return hash_code

def reverse_sort_order(tree):
    a_list = get_tree_inorder(tree)
    a_list.reverse()
    return a_list

def get_bst_list_order(tree):
    a_q = Queue()
    a_q.enqueue(tree)
    a_list = []
    while not a_q.is_empty():
        value = a_q.dequeue()
        a_list.append(value.get_data())
        if value.get_left() != None:
            a_q.enqueue(value.get_left())
        if value.get_right() != None:
            a_q.enqueue(value.get_right())
    return a_list
