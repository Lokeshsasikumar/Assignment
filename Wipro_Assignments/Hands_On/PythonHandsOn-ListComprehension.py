
# Exercise 1: Create a list of squares for numbers 1 through 10 using a list comprehension
squares = [x**2 for x in range(1, 11)]
print(f"Squares: {squares}")

# Exercise 2: Create a list of even numbers between 1 and 20 using a list comprehension
evens = [x for x in range(1, 21) if x % 2 == 0]
print(f"Even numbers between 1 and 20: {evens}")

# Exercise 3: Create a list of tuples where each tuple contains a number and its square, for numbers 1 to 5
tuples = [(x, x**2) for x in range(1, 6)]
print(f"Tuples of number and square: {tuples}")


# Exercise 4: Create a dictionary where the keys are numbers from 1 to 5 and the values are their squares
squares_dict = {x: x**2 for x in range(1, 6)}
print(f"Squares dictionary: {squares_dict}")

# Exercise 5: Create a dictionary where keys are letters and values are their ASCII values
ascii_dict = {chr(x): ord(chr(x)) for x in range(65, 91)}  # A-Z
print(f"ASCII dictionary: {ascii_dict}")


# Exercise 6: Create a set of all even numbers from 1 to 20 using a set comprehension
even_set = {x for x in range(1, 21) if x % 2 == 0}
print(f"Set of even numbers from 1 to 20: {even_set}")

# Exercise 7: Create a set of unique vowels from a given string using a set comprehension
input_string = "Hello World"
vowels_set = {char for char in input_string if char in 'aeiouAEIOU'}
print(f"Unique vowels in the string: {vowels_set}")


# Exercise 8: Create a generator that generates squares for numbers 1 to 10
squares_gen = (x**2 for x in range(1, 11))
print(f"Squares generator: {list(squares_gen)}")

# Exercise 9: Use a generator to generate Fibonacci numbers up to 100
def fibonacci_generator(limit):
    a, b = 0, 1
    while a <= limit:
        yield a
        a, b = b, a + b

fib_gen = fibonacci_generator(100)
print(f"Fibonacci numbers up to 100: {list(fib_gen)}")

# Exercise 10: Write a generator that yields numbers that are divisible by 3 from 1 to 50
div_by_3_gen = (x for x in range(1, 51) if x % 3 == 0)
print(f"Numbers divisible by 3 from 1 to 50: {list(div_by_3_gen)}")


# Exercise 11: Create a class `CountDown` that takes an integer `n` and iterates down from n to 1
class CountDown:
    def __init__(self, n):
        self.n = n

    def __iter__(self):
        self.current = self.n
        return self

    def __next__(self):
        if self.current <= 0:
            raise StopIteration
        current_value = self.current
        self.current -= 1
        return current_value

countdown = CountDown(5)
print(f"CountDown from 5: {[x for x in countdown]}")

# Exercise 12: Implement an iterator that yields the first `n` even numbers
class EvenNumbers:
    def __init__(self, n):
        self.n = n
        self.current = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.current >= self.n:
            raise StopIteration
        current_value = self.current * 2
        self.current += 1
        return current_value

even_numbers = EvenNumbers(5)
print(f"First 5 even numbers: {[x for x in even_numbers]}")

# Exercise 13: Write a simple decorator that prints "Before function" and "After function" around a function call
def simple_decorator(func):
    def wrapper():
        print("Before function")
        func()
        print("After function")
    return wrapper

@simple_decorator
def say_hello():
    print("Hello!")

say_hello()

# Exercise 14: Write a decorator `timing_decorator` that times how long a function takes to run
import time

def timing_decorator(func):
    def wrapper():
        start_time = time.time()
        func()
        end_time = time.time()
        print(f"Execution time: {end_time - start_time:.6f} seconds")
    return wrapper

@timing_decorator
def slow_function():
    time.sleep(1)

slow_function()

# Exercise 15: Create a decorator that logs the name of the function being executed and its arguments
def logging_decorator(func):
    def wrapper(*args, **kwargs):
        print(f"Function '{func.__name__}' called with arguments {args} and {kwargs}")
        return func(*args, **kwargs)
    return wrapper

@logging_decorator
def add(a, b):
    return a + b

print(f"Add result: {add(5, 3)}")


# Exercise 16: Write a lambda function that adds two numbers
add_lambda = lambda x, y: x + y
print(f"Sum of 5 and 3 using lambda: {add_lambda(5, 3)}")

# Exercise 17: Write a lambda function that returns the maximum of two numbers
max_lambda = lambda x, y: x if x > y else y
print(f"Max of 5 and 3 using lambda: {max_lambda(5, 3)}")

# Exercise 18: Use a lambda function with `filter()` to get all even numbers from a list
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
evens_filtered = list(filter(lambda x: x % 2 == 0, numbers))
print(f"Even numbers using filter: {evens_filtered}")

# Exercise 19: Use a lambda function with `map()` to square each element in a list of numbers
squares_mapped = list(map(lambda x: x**2, numbers))
print(f"Squares using map: {squares_mapped}")


# Exercise 20: Use a list comprehension to create a list of squares for even numbers from 1 to 20
even_squares = [x**2 for x in range(1, 21) if x % 2 == 0]
print(f"Squares of even numbers from 1 to 20: {even_squares}")

# Exercise 21: Use a generator expression inside a `sum()` function to get the sum of squares for numbers 1 to 5
sum_of_squares = sum(x**2 for x in range(1, 6))
print(f"Sum of squares from 1 to 5: {sum_of_squares}")

# Exercise 22: Apply a decorator to a function that uses a generator
@logging_decorator
def generate_numbers():
    for i in range(5):
        yield i

print("Generator output:")
for num in generate_numbers():
    print(num)
