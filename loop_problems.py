#1. Write a Python program to find those numbers which are divisible by 7 and multiples of 5, between 1500 and 2700 (both included).

for i in range(1500,2500):
    if i%7 ==0 and i%5==0:
        print(i)

# 2. Write a Python program to convert temperatures to and from Celsius and Fahrenheit.

a = input("enter the input: ")
last_char = a[-1]

if last_char == "c" or last_char == "C":
    fahr = int(round((9 * int(a[:-1])) / 5 + 32))
    print("fahrenheit:", fahr)
elif last_char == "f" or last_char == "F":
    cel = int(round((int(a[:-1]) - 32) * 5 / 9))
    print("celsius:", cel)
else:
    print("Invalid input. Please enter a valid temperature (e.g., 32C or 75F).")

# 3. Write a Python program to guess a number between 1 and 9.
to_find=12
while True:
    if a==to_find:
        print("correctly guessed")
        break
    else:
        a=int(input("enter the number to guess the answer "))
        
# 4. Write a Python program to construct the following pattern, using a nested for loop.

# * 
# * * 
# * * * 
# * * * * 
# * * * * * 
# * * * * 
# * * * 
# * * 
# *

for i in range(5):
    for j in range(i):

        print("*",end="") #By default, the print function ends with a newline. Passing the whitespace to the end parameter (end=' ') indicates that the end character has to be identified by whitespace and not a newline.
    print(' ')
for i in range(5,0,-1):
    for j in range(i):
        print("*",end="")
    print(" ")

# 5. Write a Python program that prints all the numbers from 0 to 6 except 3 and 6.
# Note : Use 'continue' statement.
# Expected Output : 0 1 2 4 5

for i in range(7):
    if i==3 or i==6:
        continue
    else:
        print(i)

# 6.Write a Python program that accepts a string and calculates the number of digits and letters.
count_digit=0
count_letters=0
get=input("gimme some input")
for i in get:
    if i.isdigit():
        count_digit=count_digit+1
    if i.isalpha():
        count_letters=count_letters+1
print("letters :",count_letters)
print("dighits :",count_digit)

# 7.Write a Python program to construct the following pattern, using a nested loop number.
for i in range(10):
    print(str(i)*i) # i is consider as an string so that it multiples with i times.