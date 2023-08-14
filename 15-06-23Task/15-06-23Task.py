# Expected OUTPUT: 321

d = {"don": 100, "sunny": 200, "sai": 1, "shannu": 20}
sum1 = sum(d.values())
print(sum1)


->Number of occurrences of each letter present in the string in Dictionary . aabbcdeaabbceder


string = "aabbcdeaabbceder"
T = {}
for i in string:
    if i in T:
        T[i] += 1
    else:
        T[i] = 1
print(T)


->Number of occurrences of each vowel present in the given string 

string = ".aabbcdeaabbceder"
vowels = "aeiou"
count = {}
for i in string:
    if i.lower() in vowels:
        if i.lower() in count:
            count[i.lower()] += 1
        else:
            count[i.lower()] = 1
        print(i)

->Write a pro adding the student name and marks from keyboard  and create a dict also display student marks by taking student name as input.


n = int(input("Enter students number: "))  
output = {}  
for i in range(n):  
   print("Enter student Details:", i+1) 
   Roll = int(input("Entr Roll No: "))   
   name = input("Stutent Name: ")  
   marks = int(input("Student Marks: "))  
   output[Roll] = [name, marks]    
print(output)