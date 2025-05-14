
# Exercise 1: Write a test to check if adding 2 and 3 equals 5
def test_addition():
    assert 2 + 3 == 5

# Exercise 2: Write a test to check if a string "hello" is equal to "hello"
def test_string_equality():
    assert "hello" == "hello"

# Exercise 3: Write a test to check if a number is greater than 10
def test_greater_than_10():
    assert 15 > 10


# Exercise 4: Create a function `multiply(a, b)` that multiplies two numbers
def multiply(a, b):
    return a * b

# Write a pytest test to check if `multiply(2, 3)` returns 6
def test_multiply():
    assert multiply(2, 3) == 6

# Exercise 5: Write a function `is_even(n)` that returns True if the number is even, and False if odd
def is_even(n):
    return n % 2 == 0

# Write a pytest test to check if `is_even(4)` returns True and `is_even(5)` returns False
def test_is_even():
    assert is_even(4) == True
    assert is_even(5) == False


# Exercise 6: Write a parameterized test that checks if the addition of two numbers gives correct results
import pytest

@pytest.mark.parametrize("a, b, expected", [(1, 1, 2), (2, 3, 5), (10, 5, 15)])
def test_addition_parametrized(a, b, expected):
    assert a + b == expected

# Exercise 7: Write a parameterized test to check if a string is a palindrome
@pytest.mark.parametrize("word, expected", [("madam", True), ("python", False), ("racecar", True)])
def test_palindrome(word, expected):
    assert (word == word[::-1]) == expected
