#with out lambda function
# def checkEven(number):
#     return number % 2==0

# arr1=[1,2,3,4,5,6,7,8,9,10]
# even=filter(checkEven,arr1)#map

# evenArray=[]
# for i in even:
#     evenArray.append(i)
#     print(evenArray)

#----------------------------------------
#Even ,odd
l=[0,5,10,15,20,25,30]
l1=list(filter(lambda x:x%2==0,l))
print(l1)
l2=list(filter(lambda x:x%2!=0,l))
print(l2)