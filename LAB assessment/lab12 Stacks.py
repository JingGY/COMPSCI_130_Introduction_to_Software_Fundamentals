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
        if isinstance(other, list): #if a object
            return False 
        elif (self.__len__() == other.__len__()):
            for i in range(self.__len__()):
                if self.__items[i] != other.__items[i] :
                    is_same = False
        
        else:
            is_same = False

        return is_same

     
    def __str__(self):
        return "Stack: " + str(self.__items)


#7
def reverse_sentence(sentence):
    sentence_stack = Stack()
   
    for word in sentence.split():
        sentence_stack.push(word)
    
    word_list = []
    while not sentence_stack.is_empty():
        word_list.append(sentence_stack.pop())
    
    return " ".join(word_list)


print(reverse_sentence('hello world'))

#8
def is_balanced_brackets(text):
    text_list = [char for char in text]

    bracket_stack = Stack()
    bracket_open ="[{("
    bracket_close = "]})"
    for i in text_list:
        if i in bracket_open:
            bracket_stack.push(i)
        elif i in bracket_close and not   bracket_stack.is_empty():
            if bracket_close.index(i) == bracket_open.index(bracket_stack.peek()):
                bracket_stack.pop()
            else:
                return False
        elif i in bracket_close and bracket_stack.is_empty():
            return False

    if bracket_stack.is_empty():
        return True
    else:
        return False
    

print(is_balanced_brackets('a(b)c(d))e(f'))

print(is_balanced_brackets('({x})(())()'))
'''
#9
"3 4 * 6 / 3 +"
postfix_stack = Stack()
postfix_stack.push(3)
postfix_stack.push(4)
if postfix_stack.__len__() >= 2:
    num2 = postfix_stack.pop()
    num1 = postfix_stack.pop()
    new_num = num2 * num1
    postfix_stack.push(new_num)
    postfix_stack.push(6)
    print(new_num)

else:
    print("Error")

if postfix_stack.__len__() >= 2:
    num2 = postfix_stack.pop()
    num1 = postfix_stack.pop()
    new_num = num1 / num2
    postfix_stack.push(new_num)
    postfix_stack.push(3)
else:
    print("Error")

if postfix_stack.__len__() >= 2:
    num2 = postfix_stack.pop()
    num1 = postfix_stack.pop()
    new_num = num1 + num2
    postfix_stack.push(new_num)
    print(new_num)
else:
    print("Error")

'''
#10
def evaluate_postfix(postfix_list):
    operator = "+-*/%^"
    postfix_stack = Stack() 

    for i in postfix_list:
        if i not in operator:
            postfix_stack.push(int(i))
        elif i in operator:
            #print(postfix_stack)
            if postfix_stack.__len__()>=2:
                number2 = postfix_stack.pop()
                number1 = postfix_stack.pop()
                new_number = compute(number1, number2, i)
                postfix_stack.push(new_number)
            else:
                return "Error"
    return postfix_stack.pop()

def compute(number1, number2, operator):
    if operator == '+':
        return number1 + number2
    elif operator == '-':
        return number1 - number2
    elif operator == '*':
        return number1 * number2
    elif operator == '/':
        return number1 // number2
    elif operator == "%":
        return number1 % number2
    elif operator == "^":
        return number1 ** number2


print(evaluate_postfix(['2', '10', '^']))
print(evaluate_postfix(['2', '4', '3', '*', '^']))
print(evaluate_postfix(['10', '4', '2', '-', '5', '*', '+', '3', '%']))
