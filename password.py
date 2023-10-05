import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']



print("Hello there!")
length = int(input("Enter the length of the password needed: "))
alpha  = int(input("Enter the number of alphabets: "))
number = int(input("Enter the number of numericals: "))
schars = int(input("Enter the number of special characters: "))

if alpha+number+schars != length:
    print("Total number of characters is not equal to the entered length")
    exit()
p = [ ]

for i in range(alpha):
    p.append(random.choice(letters))
for i in range(number):
    p.append(random.choice(numbers))
for i in range(schars):
    p.append(random.choice(symbols))
    
password = []

for i in range(length):
    password.append(random.choice(p))

password = "".join(map(str,password))

print(f"Here is your password: {password}")