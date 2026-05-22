# Python Strings and Conditional Statements 
# Author: Kartik sharma

#----------  strings  ----------
intro_string = "this is a string.\n we are creating it in python."
tutorial_string = "apnacolledge's tutorial.\t here we go"
simple_string = """this is string"""
print(intro_string)
print(tutorial_string)

#----------  concatenation of strings  ----------
str4 = intro_string + " " + tutorial_string + " " + simple_string #this is a string. we are creating it in python. apnacolledge's tutorial. here we go this is string
print(str4)
#length of a string
print(len(str4))

#----------  indexing of a string  ----------
str5 = "this is a string with leading and trailing spaces."
print(str5[0]) #this is called positive indexing starting from the beginning of the string
print(str5[-2]) #this is called negative indexing starting from the end of the string       
print(str5[-7:-1]) #this will print the characters from index -7 to index -2

#----------  slicing of a string  ----------
print(str5[0:10]) #this will print the characters from index 0 to index 9
print(str5[10:16]) #this will print the characters from index 10 to index 15
print(str5[:10]) #print(str5[0:10]) 
print(str4[10:len(str4)]) #this will print the characters from index 10 to the end of the string

#----------  string functions  ----------
print(str5.endswith("spaces.")) #this will return true if the string ends with "spaces."
print(str5.startswith("this")) #this will return true if the string starts with "this"
print(str5.capitalize()) #this will convert the first character of the string to uppercase and the rest to lowercase
print(str5.replace("spaces", "characters")) #this will replace the word "spaces" with "characters" in the string
print(str5.replace("i", "K"))
print(str5.find("string")) #this will return the index of the first occurrence of the word "string" in the string
print(str5.count("s")) #this will return the number of times the character "s" appears in the string

#----------  conditional statements(if, elif, else statements)  ----------

# example 1
age = int(input("enter your age: "))
if (age >= 18):#if the age is greater than 18 then it will execute this block of code
    print("he can drive") #indentation is very important in python and it is used to define the scope of the code
    print("he can vote")
    if(age > 60):#if the age is greater than 60 then it will execute this block of code
        print("he can get a senior citizen discount")#nesting of if statements is also possible in python and it is used to check multiple conditions in a single block of code
elif(age < 18):#if the age is less than 18 then it will execute this block of code
    print("he cannot drive")
    print("he cannot vote")    

# example 2
number = int(input("enter a number: "))
if(number % 2 == 0):# % operator gives remainder
    print("the number is even")
else:
    print("the number is odd")

# example 3
first_number = int(input("enter first number: "))
second_number = int(input("enter second number: "))
third_number = int(input("enter third number: "))

if (first_number > second_number and first_number > third_number):
    print("the greatest number is your first number: " , number)
elif (second_number > first_number and second_number > third_number):
    print("the greatest number is your second number: " , second_number)
else: 
    print("the greatest number is  your third number: " , third_number)

# End of strings and conditional statements 

# Practice question and their solutions

# Question=1 ,store variables name ande age and then print
introduction = ("my name is kartik and i am 18 years old")
print(introduction)

# Question=2 ,take two numbers and add , subtract , multiply ,divide
a=8
b=10
print(a+b)
print(a-b)
print(a*b)
print(a/b)

# Question=3 , store a ppercentage in a variable and if percentage is more than 60 print "eligible for engineering"
a = int(input("your percentage:"))
if(a >= 60):
    print("eligible")
else:
    print("noteligible")

# Question=4 , take a string and print string , "royal" , "bengaluru" , length of string
str1="royal challengers bengalaru"
print(str1)
print(str1[0:6])
print(str1[-10:-1])
print(len(str1))

# Question=5, take input of user's name and print it
name = input("name:")
print("welcome" , name ,"to engineering arc")

# Question=6, check if virat word is present in thestring
str3="heyy i am biggest fan of cricket because of virat"
print(str3.find("virat"))

# Question=7 , take input of age and print adult and minor
age = int(input("your age:"))
if(age >= 18):
    print("adult")
else:
    print("minor")

# Question=8 , take a number and identify if it is positive ,negative and zero
number =int(input("your number to check if +ve ,-ve or zero:"))
if(number > 0):
    print("number is positive")
elif(number < 0):
    print("number is negative")
elif(number == 0):
    print("number is zero")

# Question=9 , take a number as input and identify even or odd
numbers = int(input("your number for even odd:"))
if(numbers % 2 == 0):                               
    print("your number is even")
else: 
    print("your number is odd")

# Question=10, take number's from user and print there remarks
marks = int(input("marks :"))
if(marks >= 90):
    print("topper")
elif(marks < 90 and marks >= 75):
    print("good")
elif(marks < 75 and marks >= 50):
    print("average")
else: 
    print("need comeback arc")

# End of practice question
