import os
import csv


# Exercise 1: Create a file named "example.txt" and write "Hello, World!" into it
file = open("example.txt", "w")
file.write("Hello, World!")
file.close()

# Exercise 2: Open the file "example.txt" and read its content
file = open("example.txt", "r")
content = file.read()
print(f"Content of the file: {content}")
file.close()

# Exercise 3: Append a line "This is a new line" to the file
file = open("example.txt", "a")
file.write("\nThis is a new line")

# Exercise 4: Close the file after opening it for reading or writing
file.close()


# Exercise 5: Open a file in 'w' mode and write a list of strings to it
lines = ["Hello, World!", "This is a new line.", "File operations are fun!"]
file = open("example.txt", "w")
file.writelines([line + "\n" for line in lines])
file.close()

# Exercise 6: Open a file in 'r' mode and read its content line by line
file = open("example.txt", "r")
for line in file:
    print(f"Line: {line.strip()}")
file.close()

# Exercise 7: Use 'rb' mode to read binary data from a file
# Writing binary data to a file first
file = open("example_binary.txt", "wb")
file.write(b"Binary data here!")
file.close()

# Reading binary data from the file
file = open("example_binary.txt", "rb")
binary_content = file.read()
print(f"Binary content: {binary_content}")
file.close()


# Exercise 8: Try to open a non-existent file in 'r' mode
try:
    file = open("non_existent_file.txt", "r")
    content = file.read()
    file.close()
except FileNotFoundError:
    print("Error: The file does not exist.")


# Exercise 9: Write to a file using file = open() to handle file opening and closing
file = open("with_example.txt", "w")
file.write("This file was created using file = open() statement.")
file.close()

# Exercise 10: Read the content of a file using file = open() and print each line
file = open("with_example.txt", "r")
for line in file:
    print(f"Line from 'with_example.txt': {line.strip()}")
file.close()


# Exercise 11: Write a Python list of strings to a file, one string per line
my_list = ["Python", "is", "awesome"]
file = open("list_example.txt", "w")
file.writelines([item + "\n" for item in my_list])
file.close()

# Exercise 12: Read a file and count how many times a specific word appears in it
word_to_count = "Python"
file = open("list_example.txt", "r")
content = file.read()
file.close()
word_count = content.count(word_to_count)
print(f"The word '{word_to_count}' appears {word_count} times.")

# Exercise 13: Create a CSV file with student names and grades, and then read it
# Writing to CSV
students = [["Name", "Grade"], ["Alice", 90], ["Bob", 85], ["Charlie", 92]]
file = open("students.csv", "w", newline="")
csv_writer = csv.writer(file)
csv_writer.writerows(students)
file.close()

# Reading from CSV
file = open("students.csv", "r")
csv_reader = csv.reader(file)
for row in csv_reader:
    print(row)
file.close()


# Exercise 14: Rename a file "old_name.txt" to "new_name.txt"
file = open("old_name.txt", "w")
file.write("This is an old file.")
file.close()
os.rename("old_name.txt", "new_name.txt")

# Exercise 15: Delete a file "example.txt" after confirming it exists
if os.path.exists("example.txt"):
    os.remove("example.txt")
    print("File 'example.txt' has been deleted.")
else:
    print("The file does not exist.")


# Exercise 16: Get the absolute path of a file
abs_path = os.path.abspath("new_name.txt")
print(f"The absolute path of 'new_name.txt' is: {abs_path}")

# Exercise 17: Check if a file exists before attempting to read it
if os.path.exists("new_name.txt"):
    file = open("new_name.txt", "r")
    content = file.read()
    print(f"File content: {content}")
    file.close()
else:
    print("The file does not exist.")
