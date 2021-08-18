class BinarySearchTree:
    def __init__(self, data, left=None, right=None):
        self.__data = data
        self.__left = left
        self.__right = right

    def insert_left(self, new_data):
        if self.__left == None:
            self.__left = BinarySearchTree(new_data)
        else:
            tree = BinarySearchTree(new_data, left=self.__left)
            self.__left = tree

    def insert_right(self, new_data):
        if self.__right == None:
            self.__right = BinarySearchTree(new_data)
        else:
            tree = BinarySearchTree(new_data, right=self.__right)
            self.__right = tree

    def get_left(self):
        return self.__left

    def get_right(self):
        return self.__right

    def set_left(self, left):
        self.__left = left

    def set_right(self, right):
        self.__right = right

    def set_data(self, data):
        self.__data = data

    def get_data(self):
        return self.__data
    
    def __contains__(self, value):
        if self.__data == value:
            return True
        elif value < self.__data and self.__left != None:
            return self.__left.__contains__(value)
        elif value > self.__data and self.__right != None:
            return self.__right.__contains__(value)
        else:
            return False

    def search(self, value):
        if self.__data == value:
            return BinarySearchTree(self.__data)
        elif value < self.__data and self.__left != None:
            return self.__left.search(value)
        elif value > self.__data and self.__right != None:
            return self.__right.search(value)
        else:
            return None
    
    def insert(self, value):
        if value == self.__data:
            return 
        elif value < self.__data:
            if self.__left == None:
                self.__left = BinarySearchTree(value)
            else:
                self.__left.insert(value)
        else:
            if self.__right == None:
                self.__right = BinarySearchTree(value)
            else:
                self.__right.insert(value)

def create_bst_from_list(values):
    binaryTree = BinarySearchTree(values[0])
    for i in values:
        if i != values[0]:
            binaryTree.insert(i)
            


def print_tree(tree, level):
    print(' ' * (level*4) + str(tree.get_data()))
    if tree.get_left() != None:
        print('(L)', end='')
        print_tree(tree.get_left(), level + 1)
    if tree.get_right() != None:
        print('(R)', end='')
        print_tree(tree.get_right(), level + 1)


def print_tree(tree, level):
    print(' ' * (level*4) + str(tree.get_data()))
    if tree.get_left() != None:
        print('(L)', end='')
        print_tree(tree.get_left(), level + 1)
    if tree.get_right() != None:
        print('(R)', end='')
        print_tree(tree.get_right(), level + 1)


def create_bst_from_list(values):
    binaryTree = BinarySearchTree(values[0])
    print_tree(binaryTree, 0)
    for i in values:
        if i != values[0]:
            binaryTree.insert(i)
            print_tree(binaryTree, 0)

#9
def get_bst_preorder(tree, a_list=None):
    if a_list is None:
        a_list = []
    if tree != None:
        a_list.append(tree.get_data())
        get_bst_preorder(tree.get_left(), a_list)
        get_bst_preorder(tree.get_right(), a_list)

    return a_list

def get_maximum(tree):
    if tree.get_right() == None:
        return tree.get_data
    else:
        get_maximum(tree.get_right())
