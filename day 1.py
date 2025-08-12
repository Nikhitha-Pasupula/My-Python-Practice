#  # Variables & Data Types
#  #1 . Store your name, age, and favorite hobby in variables and display them.
name = 'Deepa'
Age = 22
favourite_hobby = 'Playing chess'
print(f"My name is {name}, i'm {Age}.\nMy hobbies are {favourite_hobby}..!")
# #2. Write a program to take two integers from the user and print their sum, difference, product, and quotient.
number1 = int(input("Enter 1st number: "))
number2 = int(input("Enter 2nd number: "))
print(number1 + number2)
print(number1 - number2)
print(number1 * number2)
print(number1 //number2)
# # 3.Create a program that takes your height in meters (float) and weight in kilograms (float) and stores them in variables.

height = float(input("Enter your height: "))
kilograms  = float(input("Enter your kgs: "))
print(height)
print(kilograms)
# # Type Conversions
# #4. Write a program that takes a floating-point number as input and converts it to an integer.
#
number = 230
print(float(number))
# 5.Take your birth year as input and calculate your current age (integer).
birth_year = int(input("Enter your birth year: "))
current_age = birth_year - 2025
print(current_age)
# # 6.Convert a string containing a number (e.g., "123") into an integer and multiply it by 2.
string = "123"
print(int(string) *2)
# Take two numbers as input and display their addition, subtraction, multiplication, division, modulus, and exponent.
a = int(input("Enter a number: "))
b = int(input("Enter b number: "))
print(a+b)
print(a-b)
print(a*b)
print(a//b)
#7. Check if a number entered by the user is divisible by both 3 and 5.
number = int(input("Enter a number: "))
print(number//3)
print(number//5)
# 8.Write a program to swap two variables using a temporary variable and then without using a temporary variable.
a = 2
b = 3


# temp = a
# a = b
# b = temp
# print(f"swapping numbers are{a} and {b}")

a,b = b,a
print(f"the swapping numbers are{a} and {b}")
# 8.Write a program that checks if a number is positive, negative, or zero.
number = 0
if number >= 0:
    print("the number is positive..!")
elif number <= 0:
    print("the number is negative..!")
else:
    print("that is not a number")
# 9.Take a number as input and check if it is even or odd.
number = int(input("Enter a number:  "))
if number %2 == 0:
    print("This is even number .!")
elif number %2 !=0:
    print("This is odd number..!")
else:
    print("please enter a number.!")
# 10.Take marks of a student as input and display their grade using the following rules:
#
# 90 and above: A
#
# 80–89: B
#
# 70–79: C
#
# 60–69: D
#
# Below 60: Fail
marks = 65
if marks >= 90:
    print("Grade A")
elif marks >=80 and marks <=89:
    print("Grade B")
elif marks >=70 and marks <=79:
    print("Grade C")
elif marks >=60 and marks <=69:
    print("Grade D")
elif marks <=60:
    print("Grade Fail..!")

# 11 Print the multiplication table of a number entered by the user.
table_number = int(input("Enter a number to get the multiplication: "))
print('multiplication for the table: ',table_number)
for i in range(1,11):
    print(f"{table_number}x {i} = {table_number * i}")
# 12 Print all even numbers from 1 to 100.
for num in range(1,101):
    if num%2==0:
        print(num)
# 12 Calculate the sum of numbers from 1 to n where n is taken from the user
total = 0
n = int(input("enter number: "))
for i in range(1,n+1):
    total +=i
    print(total)


