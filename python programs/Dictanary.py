# d=dict()
# d[10]="praveen"
# d[20]='laddu'
# d[30]='puppy'
# d[40]='sonu'
# d['mummy']=80
# d.pop(40)
# print(d)


#delite function
# d={10:'laddu',20:'sonu',30:'mummy'}
# del d[20]
# print(d)

# d=dict([(10,'laddu'),(20,'praveen'),(30,'sonu'),(40,'puppy')])
# x=dict([{10,'ganesh'},{20,'praveen'},{30,'sonu'},{40,'puppy'}])
# y=dict([[60,"manggo"],[70,'banana'],[80,'apple']])
# z=dict([[12,'Tomato'],(13,'milk')])
# a=dict({(100,'bunny'),(200,"sunny")})

# print(d)
# print(x)
# print(y)
# print(z)
# print(a)

n = int(input("Enter students number: "))  
output = {}  
for i in range(n):  
   print("Enter student Details:", i+1) 
   Roll = int(input("Entr Roll No: "))   
   name = input("Stutent Name: ")  
   marks = int(input("Student Marks: "))  
   output[Roll] = [name, marks]    
print(output)