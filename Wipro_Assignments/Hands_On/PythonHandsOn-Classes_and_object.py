#1. Basic Class and Object Creation

# Exercise 1
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

person1 = Person("Alice", 30)
print(person1.name, person1.age)

# Exercise 2
class Car:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year

car1 = Car("Toyota", "Camry", 2021)
print(car1.brand, car1.model, car1.year)

# ✅ 2. Constructor and Instance Variables

# Exercise 3
class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

book1 = Book("1984", "George Orwell")
print(book1.title, book1.author)

# Exercise 4
class Book:
    def __init__(self, title, author, price=299):
        self.title = title
        self.author = author
        self.price = price

book2 = Book("Brave New World", "Aldous Huxley")
print(book2.title, book2.author, book2.price)

# ✅ 3. Methods in Classes

# Exercise 5
class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

rect1 = Rectangle(4, 5)
print(rect1.area())

# Exercise 6
class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

    def perimeter(self):
        return 2 * (self.length + self.width)

rect2 = Rectangle(4, 5)
print(rect2.perimeter())

# ✅ 4. self Parameter

# Exercise 7
class Person:
    def __init__(self, name):
        self.name = name

    def greet(self):
        print("Hello, my name is", self.name)

p = Person("John")
p.greet()

# ✅ 5. Class Methods and Static Methods

# Exercise 8
class Employee:
    @classmethod
    def company_name(cls):
        return "Tech Corp"

print(Employee.company_name())

# Exercise 9
class MathOperations:
    @staticmethod
    def add(a, b):
        return a + b

print(MathOperations.add(10, 20))

# 6. Inheritance

# Exercise 10
class Animal:
    def speak(self):
        print("Animal speaks")

class Dog(Animal):
    def speak(self):
        print("Bark")

a = Animal()
a.speak()

d = Dog()
d.speak()
