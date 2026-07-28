#  ---------- Loops in Python ----------
# Author = Kartik Sharma

# loops are used to repeat instructions
# There are two types of loops : 1.while and 2.for loops
# if we have to print "hello" multiple times we can't just write print in all those times

# Example - 1 
count = 1          # to stop the loop iterators(count variable) are used and the process is known as iteration.
while count <= 5 :
    print("hello")
    count += 1
print(count)
print("loop ended")

# ---------- Practice Question ----------
# Queston 1
# Print numbers from 1 to 100 
a = 1
while a <= 100:
    print(a)
    a += 1
print("Answer-1 ended")

# Question 2
# Print numbers from 100 to 1
b = 100
while b >= 1:
    print(b)
    b -= 1
print("Answer-2 ended")

# Question 3
# Print the multiplication table of number 3
n = int(input("enter number :"))
i = 1
while i <=10:
    print(n, "x", i, "=", n * i)
    i +=1
print("Answer-3 ended")

# Question 4 
#  Print the elements of the following list using loop 
# [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
m = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
idx = 0
while idx < len(m):
    print(m[idx])
    idx += 1 

# Method 2 of solving question 4
c = 1
while c <= 10:
    print(c**2)
    c += 1

# Question 5
# Search for a number x in this tuple using loop
# (1, 4, 9, 16, 25, 36, 49, 64, 81, 100)
nums = (1, 4, 9, 16, 25, 36, 49, 64, 81, 100)

x = 36
i = 0
while i < len(nums):
    if(nums[i] == x):
        print("fount at index", i)
    i += 1

# ---------- Break ----------
# used to terminate the loop when encountered.
k = 1
while k <= 5:
    print(k) 
    if(k == 3):
        break
    k += 1
    
print("loop ended")

# ---------- Continue -----------
# terminates execution in the current iteration and continue execution of the loop with the next iteration.
p = 0
while p <= 5:
    if(p == 3):
        p += 1
        continue   # it acts as skip
    print(p)
    p += 1
print("loop ended")

# ---------- FOR loops ----------
# these loops are used for sequential traversal. for traversing list, string, tuples etc.
vehicles = ["car", "bike", "airplane", "scooter"]
for num in list:
    print(num)

text = "kartiksharma"
for char in str:
    print(char)
else:                 #else is used for those cases in which break is used
    print("end")

# Question = 6
# print the elements of the following list using a loop:
# [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
nums = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 49]
for el in nums:
    print(el)

# Question = 7
# search for a number x in this tuple using loop
# [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
x = 49
indx = 0
for el in nums:      # linear search
    if(el == x):
        print("number found at indx:" , indx)
    indx += 1    

# ---------- Range -----------
# range function returns a sequence of numbers, starting from 0 by default and increments by 1(by default),
# and stops before a specified number.
# start = 0 (optional)
# step = 1 (optional)
# end = 5

for z in range(10):
    print(z)
for z in range(2, 10):
    print(z)
for Z in range(2, 10, 2):
    print(Z)

# 3 Questions are left here

# ---------- pass statement ---------
# it is a null statement that does nothing, it is used as a placeholder for future code.

for f in range(5):
    pass
print("some useful work")

# 2 Question are left here

# ---------- End of loops in python ----------
