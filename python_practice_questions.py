# Python Practice Questions
# Author: Kartik Sharma

# ---------- Question 1 ----------
# wap to ask the user to enter names of their 3 favorite movies & store them in list

movie1 = input("your favourite movie:" )
movie2 = input("your second fav movie:")
movie3 = input("your third fav. movie:")
movie_list = [movie1, movie2, movie3,]
print(movie_list)

# ---------- method 2 for question = 1 ----------

movies = []
mov1 = input("enter 1st movie:")
mov2 = input("enter 2nd movie:")
mov3 = input("enter 3rd movie:")
movies.append(mov1)
movies.append(mov2)
movies.append(mov3)
print(movies)

# ---------- Question = 3 ----------
#  wap to check if a list contains a palindrome of elements. ( use : copy() method)

list1 = [1, 2, 3, 2, 1]
list2 = [1, "abc", 1]

copy_list = list1.copy()
copy_list.reverse()
if(copy_list == list1):
    print("palindrome")
else:
    print("not palindrome")

copy_list = list2.copy()
copy_list.reverse()
if(copy_list == list2):
    print("definitely palindrome")
else:
    print("not palindrome")

# ---------- Question = 4 ----------
# WAP to count the number of students with the "a" grade in the following tuple
#["c", "d", "a", "a", "b", "b", "a"]

alphabets = ["c", "d", "a", "a", "b", "b", "a"]
print(alphabets)
print(alphabets.count("a"))
alphabets.sort()
print(alphabets)


# ---------- Question = 5 ----------
# store following word meanings in python dict. 
# table:"a piece of furniture","list of facts and figures"
# cat:"a small animal"
















# ---------- Question = 6 ----------
# you are given a list of subjects for students. assure one classroom is req. for 1 subject and how many classrooms are needed
# "python", "java", "c++", "python", "javascript", "java", "python", "java", "c++", "c"




















# ---------- Question = 7 ----------
# wap to enter marks of 3 subjects from the user and store them in dictionary.
# start with an empty dictionary & add one by one. use subject name as key % marks as value




















# ---------- Question = 8 ----------
# figure out a way to score 9 & 9.0 as separate values in the set.
# (you can takehelp of built-in data tuypes )












