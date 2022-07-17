# random order password generator
import random

letter = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v",
          "w", "x", "y", "z", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R",
          "S", "T", "U", "V", "W", "X", "Y", "Z"]
numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
symbols = ["!", "#", "$", "%", "&", "(", ")", "*", "+"]

print("Welcome to the Py password generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input("How many symbols would you like in your password?\n"))
nr_numbers = int(input("How many numbers would you like in your password?\n"))

password_list = []

for l in range(1, nr_letters + 1):
    random_char = random.choice(letter)
    password_list.append(random_char)

for n in range(1, nr_numbers + 1):
    random_number = random.choice(numbers)
    password_list.append(random_number)

for s in range(1, nr_symbols + 1):
    random_symbols = random.choice(symbols)
    password_list.append(random_symbols)

random.shuffle(password_list)

password = ""
for p in password_list:
    password += p

print(password)
