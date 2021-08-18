#1 2
class Node:
    def __init__(self, init_data, init_next_node = None):
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
        while current !=  None:
            the_sum += current.get_data()
            current = current.get_next()
        return the_sum

#6
def create_sample_node_chain():
    head = Node("three")
    second_node = Node("linked")
    third = Node("nodes")
    head.set_next(second_node)
    second_node.set_next(third)
    return head

'''
head = create_sample_node_chain()
print(head.get_data())
print(head.get_next().get_data())
print(head.get_next().get_next().get_data())
print(head.get_next().get_next().get_next())
'''
#7
def print_node_chain(node_of_chain):
    print(node_of_chain.get_data())
    current = node_of_chain.get_next()
    while current != None:
        print(current.get_data())
        current = current.get_next()
#8
def create_node_chain(values_list):
    for i in range(len(values_list)):
        if i == 0:
            the_node = Node(values_list[i])
            current = the_node
        else:
            new_node = Node(values_list[i])
            current.set_next(new_node)
            current = current.get_next()
    return the_node

'''
values = create_node_chain(['apple', 'banana', 'cherry', 'date', 'elderberry'])
print_node_chain(values)
'''
#9
def convert_to_list(first_node):
    node_list = []
    node_list.append(first_node.get_data())
    current = first_node.get_next()

    while current != None:
        node_list.append(current.get_data())
        current = current.get_next()
    return node_list 
'''
node1 = Node('hello')
node2 = Node('world')
node3 = Node('goodbye')
node1.set_next(node2)
node2.set_next(node3)
print_node_chain(node1)
a_list = convert_to_list(node1)
a_list.append(100)
print_node_chain(node1)
print(a_list)
'''
#10
def get_consecutive_sum(first_node):
    sum_list = []
    the_sum = first_node.get_sum()
    sum_list.append(the_sum)
    current = first_node.get_next()
    while current != None:
        the_sum = current.get_sum()
        sum_list.append(the_sum)
        current = current.get_next()
    return sum_list

node1 = Node(4)
node2 = Node(3, node1)
node3 = Node(2, node2)
node4 = Node(1, node3)
print_node_chain(node4)
print(get_consecutive_sum(node4))
