# Program 1: Display Personal Details Using Variables
# Getting the Input from User
name = input()
age = int(input())
height = float(input())
# Printing the Values
print(name)
print(age)
print(height)



# Program 2: Personalized Greeting
name = input()
print(f"Hello, {name}!")



# Program 3: Add Two Numbers Read as Strings
# Taken the input as a String
a = input()
b = input()
# Converting the String into Integer
a = int(a)
b = int(b)
# Find the Sum
total = a+b
# Print the result
print(total)




# Program 4: Float to Integer Conversion
# float: Numbers with decimal value
# int: Whole numbers without any decimal or fractional value
# Reading a Float value from the user
n = float(input())
# Print the float value
print(n)
# Convert the float into Interger : Decimal point values will be removed
new = int(n)
# Print the result
print(new)




# Program 5: Sum Using Arithmetic Operator
# reading 2 integers from the user
a =int(input())
b = int(input())
# Finding the sum and printing the result
print(a+b)




# Program 6: Area of a Rectangle
# Reading input from the user
length = float(input())
breadth = float(input())
# Calculating the area of a rectangle
area = length * breadth
# print the result
print(area)




# Program 7: Quotient and Remainder
# User inputs
a = int(input())
b = int(input())
# find the quotient
q = a/b
# find the remainder
r = a%b
# Print the result
print(q)
print(r)




# Program 8: Power Calculation
# reading user input
base = int(input())
exponent = int(input())
# Calculate the power of and print the result
print(base ** exponent)




# Program 9: Average of Three Numbers
# Taking 3 integer numbers from the user
n1 = int(input())
n2 = int(input())
n3 = int(input())
# Find the total
total = n1+n2+n3
# Find the Average
avg = total/3 # Division Operator / --> always gives the result as a float.
# Print the Average
print(avg)
print(total)




# Program 10: Greater Than Comparison
# read 2 integer numbers from user
a = int(input())
b = int(input())
# Check wether the 1st number is greater than the 2nd number
print(a>b)




# Program 11: Equality Check
# Check whether bothe the numbers are same or not
# If the numbers are same - True
# IF the numbers are different - False
# Reading the input from the user
n1 = int(input())
n2 = int(input())
print(n1==n2)




# Program 12: Both Numbers Positive Check
# If the number is greater than 0
# Logical and --> If all the combining conditions are True , result is True
# Reading the input from the user
n1 = int(input())
n2 = int(input())
print(n1>0 and n2>0)



# Program 13: At Least One Even Number
# Even Number: If the number is divisible by 2 (Without any reminder)
# Logical or --> If any one of the combining condition is True, then the result is True.
# Arithmetic Operators
# / --> Division - result is in form of decimal value
# Example: 13/2 = 6.5
# // --> Floor Division - result is in form of integer
# Example: 13//2 = 6
# % --> Modulo - result is the remainder of the division operation
# Example: 13%2 = 1

# Reading the input from the user
n1 = int(input())
n2 = int(input())
print(n1 % 2 == 0 or n2 % 2 == 0)

# Program 14: Logical NOT on a Condition
# Logical not --> reverse the result
# True --> False
# False --> True
# Reading the input from the user
num = int(input())
print(not(num > 0))




# Program 15: Augmented Assignment Operations
# Read a number from the user
a = int(input())  # 20
a = a + 5  # a = 20 + 5 --> 25
a = a * 2  # a = 25 * 2 --> 50
a = a - 3  # a = 50 - 3 --> 47
print(a)




# Program 16: Exchange Values of Two Variables
# Reading the input from the user
a = int(input())
b = int(input())

# Logic 1 - Using temp variable
temp = a
a = b
b = temp
print(a)
print(b)

# Logic 2: Without using temp (3rd variable)
a=a+b
b=a-b
a=a-b
print(a)
print(b)

# Logic 3: Without using temp (3rd variable)
a = a^b
b = a^b
a = a^b
print(a)
print(b)

# Logic 4: Without using temp (3rd variable)
# Problem: It cannot handle 0
a = a*b
b = a/b
a = a/b
print(a)
print(b)

# Logic 5: Using Python's Special
# Simplest Way
a,b = b,a
print(a)
print(b)




# Program 17: Calculate Simple Interest
# Formula: (Principle * Rate * Time) / 100
# User Inputs
principle = float(input()) # Loan amount
rate = float(input()) # rate of interest
time = float(input()) # repayment time
# Calculate Interest
si = (principle * rate * time) / 100
# print the result
print(si)



# Program 18: Temperature Conversion (Celsius to Fahrenheit)
# Formula: F = (C * 9 / 5) + 32
# Read the temperature in Celsius
c = float(input())
# Convert the Celsius to Fahrenheit
f = (c * 9 / 5) + 32
print(f)



# Program 19: Check Divisibility by 3 and 5
n = int(input())
print(n%3==0 and n%5==0)



# Program 20:  Sum of Digits of a Two-Digit Number
num = int(input())  # num = 48
tens = num//10  # tens =  48//10 = 4
units = num%10  # units = 48%10 = 8
total = tens + units # total = 4+8 = 12
print(total)
