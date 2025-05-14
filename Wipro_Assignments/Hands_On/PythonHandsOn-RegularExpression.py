import re

#Exercise 1: Check if the string "hello" exists in the sentence "Hello, world!"
text1 = "Hello, world!"
print(re.search(r"hello", text1, re.IGNORECASE))

#Exercise 2: Search for any number in the string "There are 123 apples"
text2 = "There are 123 apples"
print(re.search(r"\d+", text2))

#Exercise 3: Extract the first email from the text "Contact me at test@example.com for more info"
text3 = "Contact me at test@example.com for more info"
match = re.search(r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}", text3)
print(match.group() if match else None)

#Exercise 4: Extract all words starting with a capital letter from the string "This is an Example Sentence"
text4 = "This is an Example Sentence"
print(re.findall(r"\b[A-Z][a-z]*\b", text4))

#Exercise 5: Check if a string contains a valid phone number format (e.g., 123-456-7890)
text5 = "My number is 123-456-7890"
print(re.search(r"\b\d{3}-\d{3}-\d{4}\b", text5))

#Exercise 6: Validate if a string is a valid email address
text6 = "example@domain.com"
print(re.match(r"^[\w\.-]+@[\w\.-]+\.\w{2,}$", text6))

#Exercise 7: Replace all occurrences of "apple" with "orange"
text7 = "I like apple pie and apple juice"
print(re.sub(r"apple", "orange", text7))

#Exercise 8: Remove all non-digit characters from a phone number string like "123-456-7890"
text8 = "123-456-7890"
print(re.sub(r"\D", "", text8))

#Exercise 9: Find all the digits in the string "abc123def456ghi"
text9 = "abc123def456ghi"
print(re.findall(r"\d", text9))

#Exercise 10: Find all the uppercase letters in the string "Python is FUN"
text10 = "Python is FUN"
print(re.findall(r"[A-Z]", text10))

#Exercise 11: Extract the area code from a phone number string like "(123) 456-7890"
text11 = "(123) 456-7890"
match = re.search(r"\((\d{3})\)", text11)
print(match.group(1) if match else None)

#Exercise 12: Extract both the month and year from a string like "March 2021"
text12 = "March 2021"
match = re.search(r"(\w+)\s(\d{4})", text12)
print(match.groups() if match else None)

#Exercise 13: Check if a string starts with "Hello" and ends with "world"
text13 = "Hello beautiful world"
print(re.match(r"^Hello.*world$", text13))

#Exercise 14: Check if a string contains only digits
text14 = "123456"
print(re.match(r"^\d+$", text14))
