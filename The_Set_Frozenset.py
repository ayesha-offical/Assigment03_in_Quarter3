# The Set Data Type

# Set is one of 4 built-in data types in Python used to store collections of data, the other 3 are List, Tuple, and Dictionary, all with different qualities and usage.

# A set is:

# unordered
# unchangeable
# unindexed
# An object cannot appear more than once in a set, whereas in List and Tuple, same object can appear more than once.

my_set: set={123,456,787}
my_set2:set = set([123,456,787])
print("my_set", my_set)
print("my_set2",my_set2)
print("My_set Type:",type(my_set))
print("My_set2 Type:",type(my_set2))
print("my_set == my_set2 = ", my_set == my_set2)


# my_set = {[123, 452, 5, 6]} # TypeError: unhashable type: 'list'
# print(my_set)


# It can hold multiple data types at once.

my_set3: set = {123, "Hello", 456, 787.5,True}
print("my_set3", my_set3)

# The set is unordered
# Note that items in the set collection may not follow the same order in which they are entered. The position of items is optimized by Python to perform operations over set as defined in mathematics.

setofunordered: set = {"a", "b"}

print(setofunordered)

# The set is Unchangeable

# As we can see, sets are unordered and unchangeable. If you want to preserve the order of items, use a list instead of a set.
# Once a set is created, you cannot change its items, but you can remove items and add new items.

# print(setofunordered[0]) # TypeError: 'set' object is not subscriptable


# to remove set items

setofunordered.remove("a")

print("After remove items from set:",setofunordered)

# to add set items

setofunordered.add("c")

print("After add items to set:",setofunordered)

# discard items from set 

setofunordered.discard({"c","b"})

print("After discard items from set:",setofunordered)

# Use difference_update() method to remove multiple element at once.

diffset:set={1,2,3,4,"A","B","C","D"}
diffset.difference_update([1,3,"C", "A"])

print("After difference_update items from set:",diffset)

# Use Update method to update

diffset.update([5,6,7])

print("After update items from set:",diffset)

# Using the union() method or | operator:

set1: set = {1, 2, 3}
set2: set = {3, 4, 5}

union_set = set1.union(set2)

print("Union of set1 and set2:", union_set)

# Using the | operator
# The | operator is a binary operator that can be used to combine two sets into a single set. It has the same effect as the union() method, but is often more concise and readable.
union_set2:set = set1 | set2

print("Union of set1 and set2 using | operator:", union_set2)

# Unique Elements
# Note that sets only store unique elements, so if you try to add a duplicate item, it will be ignored. For example:

set3: set = {1, 2, 2, 3, 3, 3}

print("Set with duplicate elements:", set3)

# discard() and remove() methods
# In Python, both discard() and remove() methods are used to remove items from a set. However, there is a key difference between the two methods:

# remove() method:

# The remove() method removes the specified item from the set.
# If the item is not found in the set, it raises a KeyError.
# This method is suitable when you are sure that the item exists in the set.
# discard() method:

# The discard() method also removes the specified item from the set.
# However, if the item is not found in the set, it does not raise any error. It simply does nothing.
# This method is suitable when you are not sure if the item exists in the set.
# Here's an example to illustrate the difference:

# Use discard() when you are not sure if the item exists in the set and you want to avoid raising an error if it does not exist.


set4: set = {1, 2, 3, 4, 5}

set4.remove(3)  # Raises KeyError: 3

print("After remove(3) operation:", set4)

# The Inner Working of SET (Advance Topic)

# A set is implemented as a hash table, which means that it uses a hash function to map keys to their corresponding values. In Python, the hash function is used to calculate the index of a key in the hash table.

exset1: str = "Hello! World"
exset2: str = "Hello! World"

print("id(a) = ", id(exset1))
print("id(b) = ", id(exset2))


print("hash of exset1: ",hash(exset1))

print("hash of exset2: ",hash(exset2))

# Important Note:
# Even if a set only allows immutable items, the set itself is mutable. Hence, add/delete/update operations are permitted on a set object

# In Python, a dictionary key must be an immutable object, meaning its value cannot be changed after it's created. This is because dictionaries use a hash table to store key-value pairs, and mutable objects cannot be hashed.

# Lets pass the set as key in dictionary which only accept immutable item as a key.


# TypeError: unhashable type: 'set'
# my_set: set   = {1,2,3,4,5, "Hello! World"}
# my_dict: dict = {my_set: "Hello! World"} # dictionary only accept immutable objects as a key
# print(my_dict)


# Example: How Set Order Can Change Dynamically

my_set: set = {1, 2, 3, 4, 5}

print("Original Set:", my_set)

my_set.add(6)

print("After adding 6:", my_set)

my_set.remove(3)

print("After removing 3:", my_set)

# Why Does the Order Change?
# New elements may trigger rehashing, leading to reallocation of storage.

# Removing an element can also affect the layout, especially if rehashing is triggered due to shrinking.

# Does This Mean Sets Are Ordered Internally?
# 🚫 No.

# Even though elements are stored based on their hash values, this does not mean sets are ordered in the way lists or tuples are. Order can change unexpectedly, so it’s unreliable for ordered operations like indexing.

# Conclusion
# Hashing determines where elements are stored, but this structure is not stable across operations.

# Adding or removing elements can trigger rehashing, which causes internal storage reallocation and an unpredictable order.


# The Frozenset

# In Python, a frozenset is an immutable (unchangeable) version of a set. It is a collection of unique elements, just like a set, but it cannot be modified after it is created.

# Here are the key features of a frozenset:

# Immutable: A frozenset cannot be modified after it is created. You cannot add, remove, or change elements in a frozenset.
# Ordered: Like sets, frozensets are unordered in Python versions before 3.7. However, from Python 3.7 onwards, frozensets maintain their insertion order, just like sets.
# Hashable: frozensets are hashable, meaning they can be used as keys in dictionaries or elements in other sets.
# Unique elements: A frozenset can only contain unique elements, just like a set.
# Here are the key differences between a set and a frozenset in Python:

# Immutability:

# set: Mutable (can be modified after creation)
# frozenset: Immutable (cannot be modified after creation)
# Modification methods:

# set: Supports methods like add(), remove(), discard(), clear(), pop(), update()
# frozenset: Does not support any modification methods
# Hashability:

# set: Not hashable (cannot be used as keys in dictionaries or elements in other sets)
# frozenset: Hashable (can be used as keys in dictionaries or elements in other sets)
# Thread safety:

# set: Not thread-safe (multiple threads can modify the set simultaneously, leading to inconsistencies)
# frozenset: Thread-safe (since it's immutable, it's safe to access from multiple threads)
# Syntax:

# set: Created using the set() function or the {} syntax (e.g., my_set = {1, 2, 3})
# frozenset: Created using the frozenset() function (e.g., my_frozenset = frozenset([1, 2, 3]))
# Use cases:

# set: Suitable for situations where you need to frequently add or remove elements (e.g., when filtering data)
# frozenset: Suitable for situations where you need an immutable collection (e.g., when using it as a key in a dictionary or as an element in another set)
# Here's a summary of the differences:

# Feature	Set	Frozenset
# Immutability	Mutable	Immutable
# Modification methods	Yes	No
# Hashability	No	Yes
# Thread safety	No	Yes
# Syntax	set() or {}	frozenset()
# Use cases	Frequent modifications	Immutable collection


# Creating a frozen set of spells
wizar_spells = frozenset(["Fireball","Teleport","Shield","Heal"])

# Trying to add a new spell (This will cause an error)
# wizard_spells.add("Lightning")  # ❌ AttributeError: 'frozenset' object has no attribute 'add'


# Checking if a spell exist

if "Fireball" in wizar_spells:
    print("The Wizard🧙 KNow Fireball💥")

 # Using frozen set as a dictionary key (allowed because it's immutable)

spell_power = {wizar_spells: "High"}    

print("The Wizard's 🧙 spells and their power🎆:", spell_power)


# Set Methods

# 🕵️‍♂️ Agents and their classified information


agent_A:set ={"Secret Mission Alpha", "Hidden Base Location", "Cipher Code", "Spy Gadgets", "Disguise Techniques"}
agent_B: set = {"Secret Mission Alpha", "Hidden Base Location", "Cipher Code", "Escape Plan", "Safe Houses"}
agent_C: set = {"Secret Mission Alpha", "Hidden Base Location", "Cipher Code", "Hacker Tools"}


# 🔎 Find information that **Agent A** has access to, but not **Agents B and C**

print("🛑 Unique to Agent A  = ", agent_A.difference(agent_B, agent_C))


# 🤝 Find information that **all agents** have in common
print("✅ Common among all agents = ", agent_A.intersection(agent_B, agent_C))

# 🌍 Create a **super set** of all intelligence

print("📂 Total intelligence database = ", agent_A.union(agent_B,agent_C))

# ⚠️ Find secrets **exclusive** to either Agent A or Agent B but not both
print("🔀 Unique between A and B = ",agent_A.symmetric_difference(agent_B))

# ❌ Check if Agent A and B have no secrets in common
print("🔎 Do A & B share secrets? = ",agent_A.isdisjoint(agent_B))


# 🏆 Now, assume **Agent B is a junior spy** with limited access

junior_agent = {"Secret Mission Alpha", "Hidden Base Location", "Cipher Code"}

print("🔒 Is Agent B senior to Junior Agent? = ",agent_B.issuperset(junior_agent))

# ✅ Verify if the junior agent only knows a subset of Agent A’s secrets

print("📌 Is Junior Agent a subset of A? = ",junior_agent.issubset(agent_A))


# Continue An Spy DATABASE Story

# 🕵️‍♂️ Spy Gadget Inventory

spy_gadgets_A = {"Night Vision Goggles", "Bug Detector", "Laser Pen", "Grappling Hook", "Hacking Device", "Voice Changer"}
spy_gadgets_B = {"Laser Pen", "Hacking Device", "Smoke Bomb", "Invisible Cloak", "EMP Device"}


# 🔥 12. pop(): Removes a random gadget from Set A
remove_gadgets = spy_gadgets_A.pop()

print(f"🎲 pop(): Removed gadget - {remove_gadgets}")
print(f"📦 Set A after pop(): {spy_gadgets_A}")
spy_gadgets_A.add(remove_gadgets) 
print("After Adding AN remove Gadget: ",spy_gadgets_A)

# ❌ 13. remove(): Removes a specific gadget from Set A (raises an error if not found)

spy_gadgets_A.remove("Night Vision Goggles")
print(f"🛠 remove('Night Vision Goggles'): {spy_gadgets_A}")


# 🔄 14. symmetric_difference(): Finds gadgets that are unique to each set

unique_gadgets = spy_gadgets_A.symmetric_difference(spy_gadgets_B)
print(f"🔀 symmetric_difference(): {unique_gadgets}")


# 🚀 15. symmetric_difference_update(): Updates Set A with unique gadgets

spy_gadgets_A.symmetric_difference_update(spy_gadgets_B)
print(f"🔁 symmetric_difference_update(): {spy_gadgets_A}")

# 🌍 16. union(): Merges both spy gadget sets
all_gadgets = spy_gadgets_A.union(spy_gadgets_B)
print(f"📂 union(All Unique gadgets): {all_gadgets}")


# 🎒 Player's different inventories (frozensets are immutable)

inventory_A: frozenset = frozenset(["Sword", "Shield", "Health Potion", "Bow"])
inventory_B: frozenset = frozenset(["Bow", "Magic Wand", "Shield", "Mana Potion"])
inventory_C: frozenset = frozenset(["Sword", "Shield"])  # A small inventory


print(f"🎮 Player inventory A: {inventory_A}")
print(f"⚡ Player Inventory B: {inventory_B}")
print(f"🛡️ Player Inventory C: {inventory_C}")
print("\n-------\n")

# 🛠 1. difference(): Items unique to Inventory A

unique_A:frozenset = inventory_A.difference(inventory_B)
print(f"❌ Items only in A: {unique_A}")  # Output: {"Sword", "Health Potion"}

# 🎯 2. intersection(): Common items between A and B
common_items:frozenset = inventory_A.intersection(inventory_B)
print(f"🔄 Common items: {common_items}")  # Output: {"Bow", "Shield"}

# 🌍 3. union(): Merging all items from A and B
all_items:frozenset=inventory_A.union(inventory_B)
print(f"🎒 Combined inventory: {all_items}")  # Output: {"Sword", "Shield", "Bow", "Magic Wand", "Health Potion", "Mana Potion"}


# 🔀 4. symmetric_difference(): Unique items between A and B

unique_items:frozenset = inventory_A.symmetric_difference(inventory_B)
print(f"🔄 Unique between A & B: {unique_items}")  # Output: {"Sword", "Health Potion", "Magic Wand", "Mana Potion"}


# ❌ 5. isdisjoint(): Do A and B have NO common items?
print(f"🚫 No common items? {inventory_A.isdisjoint(inventory_B)}")  # Output: False

# ✅ 6. issubset(): Is Inventory C a subset of A?
print(f"🛡️ C is part of A? {inventory_C.issubset(inventory_A)}")  # Output: True


# 🔝 7. issuperset(): Does A contain everything in C?
print(f"🏆 A contains C? {inventory_A.issuperset(inventory_C)}") # True

# 📝 8. copy(): Make a backup of Inventory A
backup_Inventory: frozenset = inventory_A.copy()
print(f"📦 Backup inventory: {backup_Inventory}")

print(f"🎭 Is backup the same object? {backup_Inventory is inventory_A}")  # Output: True


# 🔥 Why is this example awesome?
# ✔ Fun & relatable for gamers 🎮
# ✔ Emojis make it exciting & readable! 😆
# ✔ Shows frozenset properties in a real-world way!



# Python Garbage Collector: 🗑️🚀
# When you create variables or objects, Python stores them in memory. 🧠💾
# But when an object is no longer needed, Python automatically removes it—this is the job of the Garbage Collector (GC)! 🗑️✨

# How does it work?
# Automatic 🚀 – You don’t need to delete objects; Python handles it automatically.
# Periodic ⏳ – GC checks from time to time which data is no longer useful.
# Reference Counting 📊 – It tracks how many times an object is being used.
# If an object’s reference count drops to 0, GC removes it.


import gc  

# Create a dictionary (some data)
my_dict_garvabge = {"name": "Ayesha", "project": "Urban Loom"}

# Print the dictionary
print("Before deleting:", my_dict_garvabge)

# Delete the dictionary
del my_dict_garvabge  
gc.collect() 
print(my_dict_garvabge) # throw error (name 'my_dict_garvabge' is not defined)
print("After deleting: The garbage collector has cleaned up! 🗑️✨")


# How This Works?
# We create a dictionary (some data). 📜
# We delete it using del. ❌
# We call the garbage collector using gc.collect(). 🗑️✨
# Python removes the deleted data from memory!

