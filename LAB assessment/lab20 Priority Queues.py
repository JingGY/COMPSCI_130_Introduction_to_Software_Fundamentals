#4
class PriorityQueue():
    def __init__(self):
        self.__binary_heap = [0]
        self.__size = 0

    def __str__(self):
        return str(self.__binary_heap)  # MUST CONVERT TO STRING

    def __len__(self):
        return len(self.__binary_heap) - 1

    def add_all(self, a_list):
        for i in a_list:
            self.__binary_heap.append(i)
        self.__size += len(a_list) - 1

    def percolate_up(self, index):
        while index // 2 > 0:
            if self.__binary_heap[index] < self.__binary_heap[index // 2]:
                self.__binary_heap[index], self.__binary_heap[index //
                                                              2] = self.__binary_heap[index // 2], self.__binary_heap[index]
            index = index // 2

    def insert(self, element):
        self.__binary_heap.append(element)
        self.__size = self.__size + 1
        self.percolate_up(self.__size)

    def get_smaller_child_index(self, index):
        if index * 2 + 1 > self.__size + 1:
            return index * 2
        else:
            if self.__binary_heap[index * 2] < self.__binary_heap[index * 2+1]:
                return index * 2
            else:
                return index * 2 + 1

    def percolate_down(self, index):
        while (index * 2) <= self.__size:
            smallest_child = self.get_smaller_child_index(index)
            if self.__binary_heap[index] > self.__binary_heap[smallest_child]:
                self.__binary_heap[index], self.__binary_heap[smallest_child] = self.__binary_heap[smallest_child], self.__binary_heap[index]
            index = smallest_child

    def create_heap_fast(self, values):
        self.__binary_heap = [0] + values
        self.__size += len(values)

        for i in range(self.__size // 2, 0, -1):
            self.percolate_down(i)
            print(i)

def foo(number):
    word = str(number % 4)
    if number % 4 == 0:
        return word
    else:
        return foo(number // 4) + word

print(foo(13))