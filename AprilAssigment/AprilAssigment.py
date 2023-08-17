# 1. Calculate the sum of all numbers from 1 to a given number.
# n = int(input('Entar a Number:'))
# sum = 0
# for i in range(1, n + 1):
#     sum += i
#     print(sum)
# -------------------------------------------------------------------------
# 2. Write a program to print multiplication table of a given number.
# n = int(input('Entar your number:'))
# for i in range(1, 21):
#     j = n * i
#     print(f"{n} x {i} = {j}")
# --------------------------------------------------------------------------
# 3: Display numbers from a list using loop
# n = [1, 2, 3, 4, 5]
# for i in n:
#     print(i)
# ---------------------------------------------------------------------------
# 3: Display numbers from a list using while loop
# n = [1, 2, 3, 4, 5]
# i = 0
# while i < len(n):
#     print(n[i])
#     i += 1
# -----------------------------------------------------------------------------
# 4. Count the total number of digits in a number.
# n = int(input('Entar your number:'))
# count = 0
# while n != 0:
#     n //= 20
#     count += 1
#     print(count)
# -------------------------------------------------------------------------------
# 5.Print list in reverse order using a loop.
# n = 'praveen'
# for i in range(len(n) - 1,-1,-1):
#     print(n[i])
# --------------------------------------------------------------------------------
# 6.Display numbers from -10 to -1 using for loop.
# for num in range(-10, 0):
#     print(num)
# -------------------------------------------------------------------------------------
# 7.Use else block to display a message “Done” after successful execution of for loop
# for num in range(-10, 0):
#     print(num)
# else:
#     print("Done")
# -------------------------------------------------------------------------------
# 8. Find the factorial of a given number.
# number = int(input("Enter a number: "))
# def factorial(n):
#     if n < 0:
#         return None
#     elif n == 0:
#         return 1
#     else:
#         result = 1
#         for i in range(1, n + 1):
#             result *= i
#         return result


# fact = factorial(number)
# if fact is None:
#     print("Factorial is not defined for negative numbers.")
# else:
#     print("Factorial of", number, "is:", fact)
# -------------------------------------------------------------------------------
# 9.Reverse a given integer number.
# number = 12345
# r = int(str(number)[::-1])
# print(r)

# s1 = "Hello world!"
# s2 = s1.split()
# result = s1[::-1]
# print(result)
#-----------------------------------------------------------------------------------
#10.write a program to display prime numbers within a range .
# l = int(input ("Enter the Lowest Range Value: "))  
# u = int(input ("Enter the Upper Range Value: "))  
  
 
# for number in range (l, u + 1):  
#     if number > 1:  
#         for i in range (2, number):  
#             if (number % i) == 0:  
#                 break  
#         else:  
#             print (number) 
# -------------------------------------------------------------------------------------

#11.Display Fibonacci series up to 10 terms.
# n = int(input("Enter the value: "))
# a = 0
# b = 1
# sum = 0
# count = 1
# print("Fibonacci Series: ", end = " ")
# while(count <= n):
#   print(sum, end = " ")
#   count += 1
#   a = b
#   b = sum
#   sum = a + b
#----------------------------------------------------------------------------------------
#12.Find the factorial of a given number.
# import math  
# def fact(n):  
#     return(math.factorial(n))  
  
# num = int(input("Enter the number:"))  
# f = fact(num)  
# print("Factorial of", num, "is", f)
#-----------------------------------------------------------------------------------------
#13.Reverse a given integer number.
# num = 1234
# reversed = 0
# #Iterate through each digit of the number
# while num != 0:
# #Get the last digit of the number
#     digit = num % 10
# #Append the digit to the reversed number
#     reversed = reversed * 10 + digit
# #Remove the last digit from the number
#     num //= 10

# print("Reversed Number: " + str(reversed))
#---------------------------------------------------------------------------------------
##14.Use a loop to display elements from a given list present at odd index positions.
# def displayoddelements(lst):
#     for i in range(1, len(lst), 2):
#         print(lst[i])


# n = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
# displayoddelements(n)

#----------------------------------------------------------------------------------------
## 14.Use a loop to display elements from a given list present at odd index positions.
# Given list
# my_list = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']#0,1,2,3,4,5,6,7,8,9

# # Loop through the list and display elements at odd index positions
# for index in range(1, len(my_list), 2):
#     print(my_list[index])
# ---------------------------------------------------------------
## 15: Calculate the cube of all numbers from 1 to a given number.

# Prompt the user to enter a number
# num = int(input("Enter a number: "))
# # Calculate the cubes using a for loop
# cubes = []
# for i in range(1, num + 1):
#     cube = i ** 3
#     cubes.append(cube)
# # Display the cubes
# print("Cubes of numbers from 1 to", num, ":")
# for cube in cubes:
#     print(cube)
# ------------------------------------------------------
## 16: Find the sum of the series upto n terms.
# Prompt the user to enter the value of n
# n = int(input("Enter the value of n: "))

# Initialize the sum variable
# sum = 0

# Calculate the sum using a for loop
# for i in range(1, n+1):
#     # Replace the following line with your series calculation logic
#     term = i  # Replace with the appropriate term calculation
#     sum += term

# Display the sum
# print("The sum of the series up to", n, "terms is:", sum)
# ------------------------------------------------------------------------------
## 17: Append new string in the middle of a given string.

# def append_in_middle(given_string, new_string):
#     midpoint = len(given_string) // 2
#     first_half = given_string[:midpoint]
#     second_half = given_string[midpoint:]
#     result = first_half + new_string + second_half
#     return result


# # Example usage
# given_string = "Hello, world!"
# new_string = "beautiful "
# result = append_in_middle(given_string, new_string)
# print(result)
# -----------------------------------------------------------------------------------
##18. Arrange string characters such that lowercase letters should come first.
# def f1(string):
#     sorted_string = sorted(string, key=lambda x: (not x.islower(), x))
#     return ''.join(sorted_string)


# string = "aBcDeFgHiJkLmN"
# a = f1(string)
# print(a)
# -------------------------------------------------------------------------------
## 19.Count all letters, digits, and special symbols from a given string
# def f2(string):
#     lettercount = 0
#     digitcount = 0
#     specialcount = 0

#     for char in string:
#         if char.isalpha():
#             lettercount += 1
#         elif char.isdigit():
#             digitcount += 1
#         else:
#             specialcount += 1

#     return lettercount, digitcount, specialcount


# string = "Hello!@#$%^ 123 World!!"
# lettercount, digitcount, specialcount = f2(string)
# print("Letters:", lettercount)
# print("Digits:", digitcount)
# print("Special Symbols:", specialcount)
# -------------------------------------------------------------
# 19.Find all occurrences of a substring in a given string by ignoring the case.
# def find_occurrences(string, substring):
#     string_lower = string.lower()
#     substring_lower = substring.lower()

#     occurrences = []
#     start_index = 0
#     while True:
#         index = string_lower.find(substring_lower, start_index)
#         if index == -1:
#             break
#         occurrences.append(index)
#         start_index = index + 1

#     return occurrences


# # Example usage
# string = "Hello, hello, hello!"
# substring = "hello"
# occurrences = find_occurrences(string, substring)
# print("Occurrences:", occurrences)
# ----------------------------------------------------------------------
# 20. Write a program to count occurrences of all characters within a string.

# def count_character_occurrences(string):
#     occurrences = {}

#     for char in string:
#         if char in occurrences:
#             occurrences[char] += 1
#         else:
#             occurrences[char] = 1

#     return occurrences


# # Example usage
# string = "Hello, world!"
# character_occurrences = count_character_occurrences(string)
# for char, count in character_occurrences.items():
#     print(f"{char}: {count}")
# ----------------------------------------------------------------------
# 24: Split a string on hyphens.
# s = "example string split"
# n = s.split("-")
# print(s)
# -----------------------------------------------------------------------
# 25: Remove empty strings from a list of strings.

# 26. Removal all characters from a string except integers.
# def f1(string):
#     result = ''
#     for i in string:
#         if i.isdigit():
#             result += i
#     return result


# s = 'a1b2c3A4567asdfghj112345543!@!@#$%^'
# output = f1(s)
# print(output)
# ------------------------------------------------------------------
# 28.Concatenate two lists index-wise
# list1 = [1, 2, 3]
# list2 = [4, 5, 6]

# s = [a + b for a, b in zip(list1, list2)]
# print(s)
# -------------------------------------------------------------------
# 29.Turn every item of a list into its square.
# n = [1, 2, 3, 4, 5]
# s = [x ** 2 for x in n]
# print(s)
# ---------------------------------------------------------------------
# 31: Add new item to list after a specified item.
# def f1(lst, item, specifieditem):
#     for i in range(len(lst)):
#         if lst[i] == specifieditem:
#             lst.insert(i + 2, item)
#             break


# mylist = [1, 2, 3, 4, 5]
# f1(mylist, 10, 3)
# print(mylist)  # Output: [1, 2, 3, 10, 4, 5]
# ---------------------------------------------------------------------
# 32.Replace lists item with new value if found.
# def replaceitem(lst, item, newvalue):
#     if item in lst:
#         index = lst.index(item)
#         lst[index] = newvalue


# my_list = [1, 2, 3, 4, 5]
# replaceitem(my_list, 5, 10)
# print(my_list)
# ---------------------------------------------------------------------
# 33. Remove all occurrences of a specific item from a list.
# def removeitem(lst, item):
#     while item in lst:
#         lst.remove(item)


# mylist = [1, 2, 3, 2, 4, 2, 5, 4]
# removeitem(mylist, 4)
# print(mylist)
# ---------------------------------------------------------------------