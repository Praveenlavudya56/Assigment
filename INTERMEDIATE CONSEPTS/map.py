# def square( element):
#     return element**2

# arr1 = [1,2,3,4,5]
# sqr = map(square,arr1)
# sqrdList = []
# for i in sqr:
#     sqrdList.append(i)
# print(sqrdList)
#------------------------------------
# Define a list of numbers
numbers = [1, 2, 3, 4, 5]

# Use the map function to square each number
squared_numbers = list(map(lambda x: x**2, numbers))

# Print the squared numbers
print(squared_numbers)
