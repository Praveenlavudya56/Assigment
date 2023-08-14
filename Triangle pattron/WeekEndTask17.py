# 1. Triangle
# n = int(input("Enter number of rows:"))
# for i in range(1, n+1):
#     print(" " * (n-i), end="")
#     print("* "*i)

# 2.incresing Triangil
# n = 5
# for i in range(n):
#     for j in range(i+1):
#         print('* ', end='')
#     print()

# 3. Decricing Triangle
# n = 5
# for i in range(n):
#     for j in range(i, n):
#         print('*', end='')
#     print()

# 4.Right Triangle
# n = 5
# for i in range(n):
#     for j in range(i, n):
#         print(' ', end='')
#     for j in range(i+1):
#         print('*', end='')
#     print()

# 5.Right side Triangil

# n = 5
# for i in range(n):
#     for j in range(i+1):
#         print(' ', end='')
#     for j in range(i, n):
#         print('*', end='')
#     print()

# 6.Hill pattern

# n = 5
# for i in range(n):
#     for j in range(n):
#         print(' ', end='')
#     for j in range(i):
#         print('*', end='')
#     for j in range(i+1):
#         print('*', end='')
#     print()

# 7.square parallel
# n = 5
# for i in range(n):
#     for j in range(n):
#         if (j == 0 or j == n-1):
#             print('*', end='       ')
#         else:
#             print('', end=' ')
#     print()

# 8.Hollow icreasing triangil
# n = 5
# for i in range(n):
#     for j in range(i+1):
#         if (i == n-1 or j == 0 or j == i):
#             print('*', end='')
#         else:
#             print(' ', end='')
#     print()

# 9.Hollow decreasing triangil
# n = 5
# for i in range(n):
#     for j in range(i, n):
#         if (i == 0 or j == i or j == n-1):
#             print('*', end='')
#         else:
#             print('*', end='')
#     print()


# 10.Right Half dimend patteran
# n = 5
# for i in range(n):
#     print('* '*(i+1))
# for i in range(n-1):
#     print('* '*(n-i-1))

# 11.Lift Half dimend patteran
# n = 5
# for i in range(n):
#     print('  '(n-i-1)+' '*(i+1))
# for i in range(n-1):
#     print('  '(i+1)+' '*(n-i-1))

# 12.Hallow dimond patteran
# n = 5
# for i in range(n):
#     print('  '*(n-i-1), end='')
#     print('* ', end='')
#     if i >= 1:
#         print('  '*(2*i-1), end='')
#         print('*', end='')
#     print()