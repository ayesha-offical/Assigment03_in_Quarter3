# Working with Lists and Tuples

# Lists in Python

# # Creating a list

# # Example of creating a list with mixed data types

names:list=["ayesha","khadija","haleema"]
favouritefoods:list=["Biryani","Meggi","WhiteKarai"]
favouritemovies:list=["Avenger","F4Thailand","Lovely Runner"]

# Accessing List Elements
print("Names:",names[0])
print("Favourite foods:",favouritefoods[1])
print("Favourite movies:",favouritemovies[0])


# Modifying Lists

favouritefoods:list=["Biryani","Meggi","WhiteKarai"]
favouritefoods[2]="Burger" # Replace "WhiteKarai" with "Burger
print("Updated favourite foods:",favouritefoods)

# List Slicing

favouritemovies:list=["Avenger","F4Thailand","Lovely Runner"]
print(favouritemovies[0:2])

# Common List Methods
names.append("Aiman")

print("Names after appending:",names)

# Removing Elements
names.remove("Aiman")

print("Names after removing:",names)

# Pop() Method
deleted = names.pop(2)

print("popping Name:",deleted)
print("Final list of name:",names)

# Sorting a List
# Default Sorting (Ascending Order)

alphabets=["a","d","f","e","c","b","g"]
alphabets.sort()

print("Sorted list:",alphabets)

# Sorting in Descending Order (reverse=True)

alphabets.sort(reverse=True)

print("Descending sorted list:",alphabets)

# Sorting by String Length (key=len)

names.sort(key=len)

print("Names sorted by length:",names)

# Sorting by Last Character (key=lambda word: word[-1])

names.sort(key=lambda word: word[-1])

print("Names sorted by last character:",names)

# Reverse Sorting

names.reverse()

print("Reversed list of names:",names)

# Iterating Over Lists

for name in names:
    print("Names in loop: ",name)


# Tuples in Python

# A tuple is an ordered, immutable (unchangeable) sequence of elements. Tuples are useful for fixed data collections.

# In Python, a tuple is an immutable data type. This means that once a tuple is created, its elements cannot be changed, added, or removed.


# Creating a tuple
my_tuple1:tuple=tuple(["ayesha","khadija","haleema"])
my_tuple2:tuple=(1,2,3,4,5,6)
mixed_tuples:tuple=("ayesha", 25,1.3,True)

# Accessing Tuple Elements

print("First element of my_tuple1:",my_tuple1)
print("First element of my_tuple2:",my_tuple2)
print("First element of mixed_tuples:",mixed_tuples)

# accesing id

print("ID of my_tuple1:",id(my_tuple1))
print("ID of my_tuple2:",id(my_tuple2))
print("ID of mixed_tuples:",id(mixed_tuples))

# Slicing a tuple

print("Sliced my_tuple2:",my_tuple2[1:4])

# Tuple length

print("Length of my_tuple1:",len(my_tuple1))
print("Length of my_tuple2:",len(my_tuple2))

# Iterating through a tuple
print("Iterating through tuple2:")
for element in my_tuple1:
    print("Element in loop: ",element)

# Checking if an item exists in a tuple
if "aiman" in my_tuple1:
        print("ayesha is in my_tuple1")
else:
        print("aiman is not in my_tuple1")

# Concatenating tuples

concatenated_tuple=my_tuple1+my_tuple2
print("Concatenated tuple:",concatenated_tuple)

# Repeating tuples

repeated_tuple=my_tuple1*2
print("Repeated tuple:",repeated_tuple)


# Nested tuples

nested_tuple=(my_tuple1,my_tuple2)
print("Nested tuple:",nested_tuple)

# Unpacking tuples

name1,name2,name3=my_tuple1
print("Unpacked names:",name1,name2,name3)

# Using tuples as keys in dictionaries (because they are immutable)

my_dict={my_tuple1: "tuple key",my_tuple2:"another tuple key"}

print("Value of my_dict with tuples:",my_dict)

#Trying to modify a tuple will result in a TypeError
# my_tuple1[0] = "watermelon" #immutable. This line will raise an error. Uncomment to test.

# tuple with index

print("Index 3 of my_tuple:",my_tuple1[2])

# tuple with count method

print("Count of 'ayesha' in my_tuple1:",my_tuple1.count("ayesha"))

# Type Hinting (a: int)

# a: int is a type hint, which suggests that the variable a is expected to be an integer.
# However, type hints are not enforced in Python. They are only for documentation and tools like linters or type checkers.
# The actual value assigned to a will still be a string, because input() always returns a string.



# Dictionaries in Python

# Creating a Dictionary

my_fav_country:dict={"South Korea","America","Dubai","Japan","Saudia Arabia"}

# Accessing Dictionary Elements

print("My Favourite Country Dictionary: ",my_fav_country)

# Adding key-value pair

thisdict:dict=dict (name="ayesha", age="17",country="Pakistan")
print(type(thisdict), " - ", thisdict)

# Accessing Values

print("Name:", thisdict["name"])
print("Age:", thisdict["age"])
print("Country:", thisdict["country"])

# Access a non-existent key

# print("City:", thisdict["city"]) # This will raise a KeyError

# Modifying a Dictionary

thisdict["city"] = "karachi"
print(thisdict)

# Deleting Items

del thisdict["city"] # This will delete the key "city" from the dictionary

print(thisdict)

#  Dictionary Methods

# keys()	Returns a list of all keys in the dictionary.	
# values()	Returns a list of all values in the dictionary.	
# items()	Returns a list of key-value pairs as tuples.	
# clear()	Removes all items from the dictionary.	
# update()	Adds or updates multiple key-value pairs from another dictionary.	

# to get keys from the dictionary
print(thisdict.keys())

# to get values from the dictionary
print(thisdict.values())

# to get items from the dictionary
print(thisdict.items())

# update()	Adds or updates multiple key-value pairs from another
thisdict.update({"country":"South korea"})

print("After Updataion",thisdict)

# clear()    Removes all items from the dictionary.

thisdict.clear()

print("After Clearing",thisdict)

# Duplicate Key Not Allowed
# Dictionaries cannot have two items with the same key:

thisdict = { "name": "John", "name": "Peter" } # This will raise a TypeError. Uncomment to test.

print(thisdict)

# Iterating Over a Dictionary

# You can loop through a dictionary using for loops.

for key in thisdict:
      print(key)

for key, value in thisdict.items():
      print(key,":" ,value)      

# Common Pitfalls
print("This is get output:",thisdict.get('names'))
print("This is get output:",thisdict.get('name_1',"Not Found"))  # Returns "Not Found" if key not found
# print(thisdict["name_1"])  # (raises a KeyError).

