# Python Lists and Tuples
# Author : Kartik sharma

#----------  lists ----------
# lists are built in data types that store multiple values
# lists are mutable whereas strings are immutable

marks = [74.4, 65.3, 45.55, 65.99, 90.45] # list of marks
print(marks)
print(type(marks))#list is the class
print(len(marks))
print(marks[0])
print(marks[1])
print(marks[2])
print(marks[3])

# str = "hello"
# print(str[0])
# str[0] = "y"   #error because change of value is not applicable in string 

student = ['kartik', 98.22 ,"delhi"]
print(student[0])
student[0] = "arjun"
print(student)
#print(student[3]) #index is not present in list

#----------  list slicing  ----------
marks1 = [23, 33, 45, 67, 89, 90]
print(marks1[1:4])
print(marks1[ :4])
print(marks1[2: ])
print(marks1[-3:-1])

#----------  list methods  ----------
numbers_list = [2, 1, 3]   
numbers_list.append(4) #mutating list
print(numbers_list)    
numbers_list.sort() #arranging list in ascending order
print(numbers_list)     
numbers_list.sort(reverse = True)
print(numbers_list)

# another example using string lists
fruits_list = ["banana", "lichi" ,"apple"]  
fruits_list.reverse()
print(fruits_list)
fruits_list.sort() 
print(fruits_list)     
fruits_list.sort(reverse = True)
print(fruits_list)
fruits_list.insert(1,"grapes")
print(fruits_list)
fruits_list.remove("lichi")
print(fruits_list)
fruits_list.pop(0)
print(fruits_list)

#----------  tuples  ----------
# tuples are built in data types that lets us create immutable sequence of values.
tup = (2, 1, 3, 4,)
print(tup[0])
print(tup[1])
#tup[0]=5   #error because tuples are immutable like string
print(type(tup))
#for single value tuple = (1,)
#if simple tuple = (1) is used then type will come int 

#----------  slicing for tuples  ----------
tupl = (1, 2, 4, 6, 5, 4, 7, 4)
print(tupl.index(4))
print(tupl.count(4))
print(tupl[1:3])

# ---------- End of Lists and Tuples ----------
