# # Assignment: Examples for Control Flow & Loops

# # The if Statement

# # Example 1: Checking if a number is positive

# num:int = 20

# if num > 12:
#         print("Number is positive")
# else:
#     print("Number is not positive")       


# # The else Statement

# num:int = 11

# if num > 12:
#         print("Number is positive")
# else:
#     print("Number is not positive")       

# # The elif Statement

# num :int= 0

# if num >0:
#       print("Number is positive")
# elif num < 0:
#       print("Number is negative")
# else:
#       print("Number is zero")            


# # Nested if Statements

# age :int=10

# if age >= 0:
#       if age >= 18:
#             print("You are an adult")
#       if age <=11:
#           print("You are a child")      
#       else:
#         print("You are a teenager")

# # Practical Examples
# try:
#     agedetector = int(input("🔍 Enter your age to detect yourself: "))
    
#     if agedetector < 0:
#         print("Invalid age - age cannot be negative❌")
#     elif agedetector <= 4:
#         print("You are a baby👶")
#     elif agedetector <= 11:
#         print("You are a child👧")
#     elif agedetector <= 18:
#         print("You are a teenager👩")
#     elif agedetector <90:
#         print("You are an adult👵")
#     elif agedetector <= 120:
#         print("You are a too Old you are going to die 😂")
#     else:
#         print("You are giant👹")
# except ValueError:
#     print("Invalid input - please enter a number⚠️")


# # Loops and Iteration in Python

# # # The for Loop

# # # Example of for loops


# rows = 10
# for i in range(1, rows + 1):
#     print(" " * (rows -i) + "🍟" * i)

    


# # # Example of for loop with else

# numbers = [1, 2, 3, 4, 5]
# for num in numbers:
#      print(num)
# else:
#      print("The loop has finished🎉")     


# #  for loop with break (Skipping else)
# numbers = [1, 2, 3, 4, 5]

# for num in numbers:
#     print(num)
#     if num == 4:
#      print("Loop with break")
#      break
# else:
#      print("The loop has finished���")

#   Searching with else

# foods=["🍕","🍔","🌭","🥗","🍙","🍜","🍛","🌭","🍦","🥪","🍣"] 
# for food in foods:  
#     if food == "🍳": 
#         print("Food Found!")
#         break 
# else:
#         print("Food not found!")


# # # The while Loop
# # # Example of while loop
# count = 0
# while count < 5:
#     print(count)
#     count += 1

# # Example of while loop with else
# count = 0
# while count < 5:
#     print(count)
#     count += 1
# else:
#     print("The loop has finished🎉")

# # Example of for loop with range

# for i in range(11):
#     print(i)

# The while Loop

# count: int=0
# while count <=10:
#     print(count)
#     count += 1

# Controlling Loops

# Break example
# for i in range(10):
#     if i == 5:
#         break
#     print(i)  

# Continue example
# for i in range(91):
#     if i == 80:
#      continue
#     print(i)


# . Nested Loops

# List of days
days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]

# List of periods for each day
periods = ["Math", "English", "Science", "History", "Computer"]

# Nested loop to display the timetable
for day in days:
    print(f"\nTime Table for {day}:")
    for period in periods:
        print(f"-{period} Class")