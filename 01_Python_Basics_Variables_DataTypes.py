# Python notes
# Author: Kartik sharma
# Topics: variables, operators, input, type casting

# to save file .py extension is used

# ----------  variables  ----------

# Variable is a container that holds a value and its name should start with a letter or underscore.
# Variable name can contain letters, numbers and underscores and should not be a keyword.
# Variable name should not contain spaces and should be descriptive.
# Variable(memory location) = Value 
# Kartik = String value and 25 is integer value and 1.3 is floating value."""

name = "kartik"
age = 25
price = 1.3
age2 = age 

print("MY NAME IS: " , name)
print("MY AGE IS: " , age2 )
print("THE PRICE IS: " , price)
print("my name is : " , name , " , my age is: " , age2 , "and the price is: " , price)

# Data types in python = string, integer, float, boolean, NoneType 
print( type(name) )   # <class 'str'> name is a string
print( type(age2) )   # <class 'int'> +ve , -ve , 0
print( type(price) )  # <class 'float'> decimal numbers

old = False 
b = None

print(type(old)) # <class 'bool'> [ only cappital True(T) and False(F) are used IN boolian data type]
print(type(b))   # <class 'NoneType'>

# ----------  Keywords  ----------

# Keywords in python are reserved words that cannot be used as variable names and they have special meaning in the language
# Some keywords are: if, while, break, continue, pass, def, return, import, from, as, class, try, except, 
# finally, with, lambda, global, nonlocal, assert, yield, del, raise, in, is, and, or, not
name1 = "kartik"
name2 = '''kartik'''
name3 = 'kartik'
print(name1)
print(name2)
print(name3)

# ---------- Expression Execution ----------

# string and numeric values can operate together with *
m,n = 2,3
txt = "@"
print(2*txt*3)    # @@@@@@

# string and string can operate with +
o,p = "2",3
txt="@"
print((o+txt)*p)  # 2@2@2@

# numeric values can operate with all arithmetic operators
m,n = 2,3
q= 4
print(a+b*c) # 14

# arithmetic expression with integer and float will result in float
r,s = 10,5.0
t = r*s
print(t) # 50.0

# result of division operator with two integer will be float [print(1/2) = 0.5{float value}]
# integer division with float and int will give int displayed as float
i,j = 1.5,3
k=i//j
print( k, i/j) # o.o , 0.5

# Floor gives closest integer , which is lesser than or equal to the float value , result of (a//b) is same as floor(a/b)
e,f = 12,5        # print(-12//5) = -3
g=e//f            
print(g) # 2

# ---------- Arithmetic operator ----------

a = 203893
b = 6938
total = a + b
print("the sum of a and b is: " , total)

diff = a - b
print("the difference of a and b is: " , diff)

product = a*b 
print("the product of a and b is: " , product)

quotient = a/b
print("the quotient of a and b is: " , quotient)

modulus = a%b
print("the modulus of a and b is: " , modulus)
# Print( a**b )    # a to the power of b

#---------- relational operator ----------

x = 10
y = 20

print( x == y )    # False
print( x != y )    # True
print( x > y )     # False
print( x < y )     # True
print( x >= y )    # False
print( x <= y )    # True

# ---------- Assignment operator ----------

num = 10
num += 5 # num = num + 5    
print(num) # 15

num -= 3 # num = num - 3
print(num) # 12

num *= 2 # num = num * 2
print(num) # 24

num /= 4 # num = num / 4
print(num) # 6.0

num %= 5 # num = num % 5
print(num) # 1.0

num **= 3 # num = num ** 3
print(num) # 1.0

#----------  Logical operator  ----------

# not > and > or
num_a = 50 
num_b = 30

print( not False )                              # True
print( not True )                               # False
print( not ( num_a > num_b) )                   # False
print( (num_a > num_b) and (num_b < 100) )      # True
print( (num_a > num_b) or (num_b > 100) )       # True
print( (num_a < num_b) and (num_b < 100) )      # False
print( (num_a < num_b) or (num_b < 100) )       # True

#----------  Input function  ----------

# They are used to take input from the user and it always returns a string
# Input converts the user input into a string and we can use type casting to convert it into other data types like int, float, etc.
named = input("enter your name: ")
ages = int(input("enter your age: "))       # Without int() it will be a string and with int() it will be an integer
marks = float(input("enter your marks: "))  # Without float() it will be a string and with float() it will be a floating
print(type(named), "welcome " , named)
print(type(ages), "your age is: " , ages)
print(type(marks), "your marks are: " , marks)

# ---------- Type conversion  ----------

num1 = 10
num2 = 3.14
total_sum = num1 + num2
print("the sum is: " , total_sum) # 13.14

num3 = "20" 
num4 = 5.2
# print(num3 + num4) # error
# Type casting
num3 = int(num3) # convert string to integer
print(num3 + num4) # 25.2

# ----------  End of session - 1 ----------
