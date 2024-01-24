#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")

#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91

Password = ""

nr_letters= int(input("How many letters would you like in your easy password?\n")) 

for l in range(0,nr_letters+1):
    Password += random.choice(letters)


nr_numbers = int(input(f"How many numbers would you like?\n"))
for n in range(0,nr_numbers+1):
    Password += random.choice(numbers)


nr_symbols = int(input(f"How many symbols would you like?\n"))
for i in range(0, nr_symbols+1):
    Password += random.choice(symbols)

print(f"Your easy password is : {Password}")



#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P

Password_list = []

hard_letters= int(input("How many letters would you like in your hard password?\n")) 
for l in range(1,hard_letters+1):
    Password_list.append(random.choice(letters))


hard_numbers= int(input("How many numbers would you like in your password?\n")) 
for i in range(1,hard_numbers+1):
    Password_list.append(random.choice(numbers))

hard_symbols= int(input("How many symbols would you like in your password?\n")) 
for i in range(1,hard_symbols+1):
    Password_list.append(random.choice(symbols))

#shuffled the list keep in mind it only shuffles the list so make sure not to use it on string variables such as Password_compile below
random.shuffle(Password_list)

#creating string from the list- 
Password_compile = ""
for i in Password_list: 
    Password_compile += i

#final 
print(f"Your hard to ccrack password is : {Password_compile}")