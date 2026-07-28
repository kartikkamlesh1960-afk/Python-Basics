# Python Dictionaries and Sets
# Author: Kartik Sharma

#----------  DICTIONARIES  ----------
# dictionaries are used to store data values in key:value pairs
# Dictionaries are mutable and unordered, and they do not allow duplicate keys

info = {
    "key" : "value",
    "subjects" : ["python", "c", "java"],
    "topics" : ("dictionaries" , "sets"),
    "name" : "apnacollege",
    "learning" : "coding",
    "age" : 35 ,
    "is_adult" : True ,
    "marks" : 76.4,
    12.5: 45 
}
empty_dict = {}
empty_dict["home"] = "sector6"
print(empty_dict)
print(info["name"])
#print(info["surname"]) #error because surname in not defined in dictionary
print(type(info))
info["name"]= "khapra"
print(info)

#----------  nested dictionaries  ----------

student ={
    "names" : "kartik sharma",
    "subjects" : {
        "phy" : 97,
        "chem" : 34,
        "maths" : 99
      }
}
print(student["subjects"]["chem"])
print(student)

#----------  dictionary methods  ----------

print(list(student.keys())) # to print all keys of dictionary .keys() is used and list is to show the output in list format
print(len(student)) #to find the number of keys used in dictionary but not the nested ones.
print(list(student.values())) #to print all values of dictionary .values() is used.
print(list(student.items())) # to print the (key:value)pairs in tuples
#print(student["namess"])    #error
print(student.get("namess")) #no error
student["subjects"]["maths"] = 44
student.update({"city": "delhi"})
print(student)

#----------  Set in python  ----------
# set is the collection of unordered items
# each element in the set must be unique and immutable
# Sets themselves are mutable because elements can be added or removed

collection = {1, 2, 2, 2, 2, 3, 4, "hello", "world"} # Duplicate values are automatically ignored in sets
print(type(collection))
print(len(collection))
print(collection)

empty_dictionary = {} # this creates an empty dictionary, not an empty set
print(type(empty_dictionary)) 
# To create an empty set 
empty_set = set()
print(type(empty_set))

#----------  set methods  ----------
aset = set()
aset.add(1)
aset.add(2)
aset.add(2)
aset.add(3)
aset.add("hello")
aset.add((123))
#aset.add([123]) # Lists cannot be added to sets because lists are mutable and unhashable
aset.remove(1)
#aset.remove(5) #error because 5 does not exist in set
print(aset)
print(len(aset))
aset.clear()
print(len(aset))
print(collection.pop())

set1 = {1, 2, 3}
set2 = {3, 4, 5}
print(set1.union(set2)) #  Combines values from both sets and returns a new set
print(set1.intersection(set2)) # Returns only common values from both sets

#----------  End of Dictionaries and Sets  ----------
