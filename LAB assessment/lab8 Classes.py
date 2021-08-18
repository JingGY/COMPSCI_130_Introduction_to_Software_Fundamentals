#1 2 3
class Rectangle:
    def __init__(self, width=10, height=10):
        self.__width = width
        self.__height = height

    def get_width(self):
        return self.__width

    def get_height(self):
        return self.__height

    def __str__(self):
        return str(self.__width) + " x " + str(self.__height)

    def __repr__(self):
        return "Rectangle("+str(self.__width) +", " +str(self.__height) +")"

    def get_area(self):
        are = self.__width * self.__height
        return are

    def get_perimeter(self):
        perimeter = self.__width * 2 + self.__height * 2
        return perimeter


r1 = Rectangle(3, 4)
print(r1.get_area())
print(r1.get_perimeter())
r3 = Rectangle()
print(r3.get_area())
print(r3.get_perimeter())

#4 - 8
import math

class QuadraticEquation:
    def __init__(self, coeff_a=1, coeff_b=1, coeff_c=1):
        self.__coeff_a = coeff_a
        self.__coeff_b = coeff_b
        self.__coeff_c = coeff_c

    def get_coeff_a(self):
        return self.__coeff_a

    def get_coeff_b(self):
        return self.__coeff_b

    def get_coeff_c(self):
        return self.__coeff_c

    def get_discriminant(self):
        self.__discriminant = self.__coeff_b **2 - 4* self.__coeff_a * self.__coeff_c
        return self.__discriminant

    def has_solution(self):
        self.__dis = self.get_discriminant()
        if self.__dis >= 0:
            return True
        else:
            return False
        
    def get_root1(self):
        self.__dis = self.get_discriminant()
        root1 = (-self.__coeff_b + math.sqrt(self.__dis))/(2*self.__coeff_a)
        return root1

    def get_root2(self):
        self.__dis = self.get_discriminant()
        root2 = (-self.__coeff_b - math.sqrt(self.__dis))/(2*self.__coeff_a)
        return root2

    def __str__(self):
        if not self.has_solution():
            return  "The equation has no roots."
        elif self.get_discriminant() == 0:
            return "The root is " + str("{:.2f}".format(self.get_root1())) + "."
        else:
            return "The roots are " + str("{:.2f}".format(self.get_root1())) + " and " + str("{:.2f}".format(self.get_root2())) + "."


equation1 = QuadraticEquation(4, 4, 1)
print(equation1)
equation2 = QuadraticEquation()
print(equation2)
equation3 = QuadraticEquation(1, 2, -63)
print(equation3)

#9 10


class Product:
    def __init__(self, product_id, product_name, product_price=1):
        self.__product_id= product_id
        self.__product_name = product_name
        self.__product_price= product_price

    def __str__(self):
        return self.__product_name+"(id = "+str(self.__product_id)+"), $"+str(self.__product_price)

    def set_product_price(self, product_price):
        if product_price >= 0:
            self.__product_price = product_price
    
    def get_product_price(self):
        return self.__product_price

    def set_product_name(self, product_name):
        self.__product_name = product_name

    def get_product_name(self):
        return self.__product_name
        
    def set_product_id(self, product_id):
        if product_id >= 0:
            self.__product_id = product_id

    def get_product_id(self):
        return self.__product_id


# 11 12
class Dog:
    def __init__(self,height):
        self.__height = height

    def get_height(self):
        return self.__height 

    def set_height(self, height):
        if height > 0:
            self.__height = height

    def speak(self, repeat=1):
        repeat_str = "Woof " * repeat
        print (repeat_str)

    def __str__(self):
        return 'I am a Dog. My height is ' + str(self.__height)




animal = Dog(27)
print(animal)
animal.set_height(53)
print("Now my height is", animal.get_height())
animal.set_height(-2)
print("My height is", animal.get_height())
animal.speak()
animal.speak(5)

class Robot:
    def __init__(self, name, start = (0, 0)):
        self.__position = start
        self.__name = name
        self.x_position = self.__position[0]
        self.y_position = self.__position[1]

    def move_to(self, x_position, y_position):
        self.x_position = x_position
        self.y_position = y_position
        

    def up(self, displacement):
        self.y_position += displacement
    
    def right(self, displacement):
        self.x_position += displacement
        
    def __str__(self):
        return self.__name + ' is at ' + str((self.x_position, self.y_position))

robot1 = Robot("Marvin")
print(robot1)
robot1.move_to(5, 11)
print(robot1)
robot1.move_to(1, 2)
print(robot1)
robot1.up(3)
robot1.right(-4)
print(robot1)

        



