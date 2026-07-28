# Python Function and Recursion 
# Author : Kartik Sharma

# ---------- FUNCTION ----------
# block of statements that perform a specific task.
# def = function defination
# a, b = parameters
# calc_sum(val1 , val2) = function call
# val1 , val2 = arguments

def cal_sum(a, b):
    total = a + b 
    print(total)
    return total

cal_sum(34, 88)
cal_sum(44, 87)

def cal_avg(c, d, e):
    Total = c + d + e
    avg = Total / 3
    print(avg)
    return avg

cal_avg(2, 3, 99)
cal_avg(45, 77, 22)

# there are two types of functions :
# 1 built-in funtions - print() len() type() range()
# 2 user defined functions - func made by users itself

# Default Parameters
# assigning a default value to parameter, which is used when no argument is passed.
def cal_prod(a=1, b=1):    # a= 1 , b= 1
    print(a*b)
    return a*b
cal_prod()  # uses default values a=1 and b=1

# question = 1
# WAF to print the length of a list (where list is the parameter)








# question = 2
# WAF to print the length of a list (where list is the parameter)








# question = 3
# WAF to find the factorial of n ( where n is the parameter)








# question = 4
# WAF to convert usd to inr.








# ---------- RECURSION ----------
# when a function calls itself repeatedly
# recursion needs:
# 1. base case (stops recursion)
# 2. recursive call (function calling itself)

def show(n):
    if(n == 0):    # base case
        return
    print(n)
    show(n-1)

show(5)
  
def fact(k):
    if(k == 0 or k == 1):
        return 1
    else:
        return k * fact(k-1)
    
print(fact(5))

# question = 5
# Write a recursive function to calculate the sum of first n natural numbers.








# question = 6
# write a recursive function to print all elements in a list (use list and index as parameteres.)












