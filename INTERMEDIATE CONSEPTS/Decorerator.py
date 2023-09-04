# def cube (func):
#     def wrapper():
#         print(3**3)
#         func()

#     return wrapper
# @cube
# def square():
#     print(5*5)
# square()
#-------------------------
# def sqaure(n):
#     print(n*n)

# n=5
# sqaure(n)
#--------------------------------------------------
# # Decorator function
# def my_decorator(func):
#     def wrapper():
#         print("Something is happening before the function is called.")
#         func()  # Call the original function
#         print("Something is happening after the function is called.")
#     return wrapper

# # Apply the decorator to the function using the @ syntax
# @my_decorator
# def say_hello():
#     print("Hello!")

# # Call the decorated function
# say_hello()
