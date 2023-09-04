# from functools import reduce

# def product(x,y):
#     return x,y


# numbers=[2,3,4,5]
# recprodact=reduce(product,numbers)
# print(recprodact)
#-----------------------------------------
numbers=[2,3,4,5]
prodact=1
for i in range(len(numbers)):
    prodact=prodact*numbers[i]
print(prodact)