# Python basic practice
# Author: Kartik sharma
# Topics: variables, operators, input, type casting

#to save file .py extension is used
#----------  variables  ----------
#variable is a container that holds a value and its name should start with a letter or underscore
#variable name should start with a letter or underscore
#variable name can contain letters, numbers and underscores and should not be a keyword
#variable name should not contain spaces and should be descriptive
#variable(memory location)=value
#kartik = string value and 25 is integer value and 1.3 is floating value

name = "kartik"
age = 25
price = 1.3
age2 = age 

print("MY NAME IS: " , name)
print("MY AGE IS: " , age2 )
print("THE PRICE IS: " , price)
print("my name is : " , name , " , my age is: " , age2 , "and the price is: " , price)

#data types in python = string, integer, float, boolean, NoneType 
print( type(name) )# <class 'str'> name is a string
print( type(age2) )# <class 'int'> +ve , -ve , 0
print( type(price) )# <class 'float'> decimal numbers

old = False 
b = None

print(type(old))# <class 'bool'>
print(type(b))# <class 'NoneType'>

#----------  keywords  ----------
#keywords in python are reserved words that cannot be used as variable names and they have special meaning in the language
#some keywords are: if, while, break, continue, pass, def, return, import, from, as, class, try, except, finally, with, lambda, global, nonlocal, assert, yield, del, raise, in, is, and, or, not
name1 = "kartik"
name2 = '''kartik'''
name3 = 'kartik'
print(name1)

print(name2)
print(name3)

#----------  arithmetic operator  ----------
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
#print( a**b ) # a to the power of b

#----------  relational operator  ----------
x = 10
y = 20

print( x == y ) #false
print( x != y ) #true
print( x > y ) #false
print( x < y ) #true
print( x >= y ) #false
print( x <= y ) #true

#----------  assignment operator  ----------
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

#----------  logical operator  ----------
num_a = 50 
num_b = 30

print( not False ) # true
print( not True ) # false
print( not ( num_a > num_b) ) # false
print( (num_a > num_b) and (num_b < 100) ) # true
print( (num_a > num_b) or (num_b > 100) ) # true
print( (num_a < num_b) and (num_b < 100) ) # false
print( (num_a < num_b) or (num_b < 100) ) # true

#----------  input function  ----------
#they are used to take input from the user and it always returns a string
#input converts the user input into a string and we can use type casting to convert it into other data types like int, float, etc.
named = input("enter your name: ")
ages = int(input("enter your age: "))#without int() it will be a string and with int() it will be an integer
marks = float(input("enter your marks: "))#without float() it will be a string and with float() it will be a floating
print(type(named), "welcome " , named)

print(type(ages), "your age is: " , ages)
print(type(marks), "your marks are: " , marks)

#---------- type conversion  ----------
num1 = 10
num2 = 3.14
total_sum = num1 + num2
print("the sum is: " , total_sum) # 13.14

num3 = "20" 
num4 = 5.2
#print(num3 + num4) # error
#type casting
num3 = int(num3) # convert string to integer
print(num3 + num4) # 25.2
