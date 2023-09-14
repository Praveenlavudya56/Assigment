import re
txt="The rain in Spain"
#find all lower case charachters alphabetically b/w "a" and "m":
x=re.findall("[a-m]",txt)
print(sorted(x))

#Date
import re
text="i will go to my friend ganesh marrige on 12/12/2023"
pattren=r'\d{2}/\d{2}/\d{4}'
match=re.findall(pattren,text)
for i in match:
    print(i)

#toll free number 1800-180-1290
import re
text='my frind mobile number is 1800-180-1290'
pattren=r'\d{4}-\d{3}-\d{4}'
matches=re.findall(pattren,text)
for i in matches:
    print(i)

#Write a Python program that matches a word containing 'z',
#  not the start or end of the word 

import re
text = "This is a test. Zoo is not at the start or end. But zebra is."
pattern = r'\b\w*z\w*\b'
matches = re.findall(pattern, text, re.IGNORECASE)
for match in matches:
    print(match)



