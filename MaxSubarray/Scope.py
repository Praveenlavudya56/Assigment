# A variable is only available from inside the region it is created. This is called scope.

# Local Scope
# A variable created inside a function belongs to the local scope of that function, and can only be used inside that function


a=12
def sum(a,b=13):
    a=14
    summ=a+14
    return summ
a=15
print(sum(a))