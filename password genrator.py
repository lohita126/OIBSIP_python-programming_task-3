import random
import tkinter as tk


letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
           'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
           'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

password = []

# Get user input
letter_length = int(input("How many letters would you like in your password? "))
number_length = int(input("How many numbers would you like in your password? "))
symbol_length = int(input("How many symbols would you like in your password? "))

# Choose characters
nr_letters = random.choices(letters, k=letter_length)
nr_numbers = random.choices(numbers, k=number_length)
nr_symbols = random.choices(symbols, k=symbol_length)

# Combine all parts
password = nr_letters + nr_numbers + nr_symbols

# Shuffle the list
random.shuffle(password)

# Join to make a string
str_password = "".join(password)

# Output
print("Your password is:", str_password)







