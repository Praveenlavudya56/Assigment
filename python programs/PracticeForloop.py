praveenkiOpstion =["mango","banana","apple","showarma","hydarabadiBriyani"]

praveenkiWish ="showarma"
print("---------------------------")
for option in praveenkiOpstion:
    if option == praveenkiWish:
        print("praveen is Happy")
        break
    elif option != praveenkiWish:
        print("praveen is Sad")