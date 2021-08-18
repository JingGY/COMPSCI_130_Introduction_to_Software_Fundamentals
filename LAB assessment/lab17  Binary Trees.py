#Q3

class BinaryTree:
    def __init__(self, data, left=None, right=None):
        self.__data = data
        self.__left = left
        self.__right = right
    def insert_left(self, new_data):
        if self.__left == None:
            self.__left = BinaryTree(new_data)
        else:
            tree = BinaryTree(new_data, left=self.__left)
            self.__left = tree
    def insert_right(self, new_data):
        if self.__right == None:
            self.__right = BinaryTree(new_data)
        else:
            tree = BinaryTree(new_data, right=self.__right)
            self.__right = tree
    def get_left(self):
        return self.__left
    def get_right(self):
        return self.__right
    def set_data(self, data):
        self.__data = data
    def get_data(self):
        return self.__data
    def set_left(self, left):
        self.__left = left
    def set_right(self, right):
        self.__right = right

def print_tree(tree, level):
    print(' ' * (level*4) + str(tree.get_data())) #print the root node
    if tree.get_left() != None:
        print('(l)', end = '')
        print_tree(tree.get_left(), level + 1)
    if tree.get_right() != None:
        print('({r)', end = '')
        print_tree(tree.get_right(), level + 1)
#q4
def add_all(a_list, index):
    btree = BinaryTree(a_list[index])
    if index * 2 + 1 <= len(a_list) - 1:
        btree.set_left(BinaryTree(a_list[index * 2 + 1]))
        add_all(a_list, index + 1)
    if index * 2 + 2 <= len(a_list) -1:
    
        btree.set_right(BinaryTree(a_list[index * 2 + 2]))
        add_all(a_list, index + 1)

    return btree

tree = add_all([10, 5, 11, 22], 0)
print_tree(tree, 0)

        
'''
def create_a_bigger_tree():
    f = BinaryTree("f")
    d = BinaryTree("d", None, f)
    g = BinaryTree("g")
    e = BinaryTree("e", None, g) #forget None
    b = BinaryTree("b", d, e)
    c = BinaryTree("c")
    a = BinaryTree("a", b, c)
    return a

a = create_a_bigger_tree()
print(a.get_data())
print(a.get_left().get_data())
print(a.get_right().get_data())
print(a.get_left().get_right().get_data())

a = create_a_bigger_tree()
print(a.get_data())
print(a.get_left().get_data())
print(a.get_right().get_data())
print(a.get_left().get_right().get_data())
print(a.get_left().get_left().get_data())
print(a.get_left().get_left().get_right().get_data())
print(a.get_left().get_right().get_right().get_data())

#q4

def add_all(a_list, index):
    root = BinaryTree(a_list[index])
    
    print(' ' * (index * 2) + str(a_list[index]))
    if a_list[index].get_left() != None:
        print('(l)', end = '')
        add_all(a_list[index].get_left(), index + 1)
    if a_list[index].get_right() != None:
        print('(r)', end = '')
        add_all(a_list[index].get_right(), index + 1)

tree = add_all([10, 5, 11, 22], 0)
print_tree(tree, 0)


#q6

def search(tree, item):
    if tree is None:
        return False
    if tree.get_data() == item:
        root = tree.get_data()
        return True
    if tree.get_data() < item:
        return search(tree.get_right(), item)
    else:
        return search(tree.get_left(), item)
        

        
    
print(search(tree2, 65))

#q7
def get_sum_string_len(my_tree):
    if my_tree == None:
        return 0
    else:
        lenTotal = len(my_tree.get_data()) + get_sum_string_len(my_tree.get_left()) + get_sum_string_len(my_tree.get_right())
        return lenTotal
    
    
my_tree = BinaryTree('berry')
my_tree.insert_left('apple')
my_tree.insert_right('banana')
print(get_sum_string_len(my_tree))

tree3 = BinaryTree("a")
tree3.set_left("b")
tree3.set_right("c")
tree3.set_left('d')
tree3.set_right('f')
tree3.set_right('e')
tree3.set_right('g')


#q8

tree2 = BinaryTree('41')
tree2.insert_left('11')
tree2.insert_left('20')
tree2.insert_right('91')
tree2.insert_right('65')
tree2.get_right().insert_left('90')
tree2.get_left().insert_right('29')


#q9
def get_min_even(b_tree):
    minNode = 9999
    if b_tree == None:
        return 9999
    else:
        if int(b_tree.get_data()) % 2 == 0 and int(b_tree.get_data()) < minNode:
            minNode = b_tree.get_data()
            return minNode
        else:
            get_min_even(b_tree.get_left())
            get_min_even(b_tree.get_right())
            

print(get_min_even(tree2))

#10
tree1 = BinaryTree(7)
tree1.insert_left(1)
tree1.insert_left(2)
tree1.get_left().insert_right(5)
tree1.insert_right(14)
tree1.insert_right(9)

def combine_trees(btree1, btree2):
    if 

'''



def insertion_sort(a_list):
    for index in range(1, len(a_list)):
        current_value = a_list[index]  # pre-store value that maybe overlapped
     # compare items every pass
        while index > 0 and a_list[index-1] > current_value:
            a_list[index] = a_list[index-1]
            index = index-1
        a_list[index] = current_value # current value is overlapped, so assign the pre-stored value to it
    return a_list

print(insertion_sort([1,4,3,7,5]))




    
