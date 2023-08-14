#for each element in sequence
# do some action

# s="sairam"
# for x in s:
#     print(x,end="-")
#---------------------------------------------------

# s=input("enter the string ")
# i=0
# for x in s:
#     print("for each charecter present in ", i , "is" , x)
#     i+=1
    

# for x in range(10):
#     print("laddu")
#------------------------------------------
# n=int(input("enter the number :"))
# for i in range(1,n+1):
#     print("*"*n)
#-----------------------------------------
n=int(input("enter the number :"))
for i in range(1,n+1):
    for j in range(1,n+1):
        print(n+1-j,end=" ")
    print()

# n=5
# for i in range(1,n+1):
#     for j in range(1,n+2-i):
#         print(n+1-j,end=" ")
#         print()
        