age=int(input ("Enter your Age: "))

if age < 18:
    print("sorry you are not eligebul for vote" )
elif age>=18 and age <=65:
    print("you are eligibul for vote")
else:
    print("You are eligible to vote, but you may choose to retire instead")