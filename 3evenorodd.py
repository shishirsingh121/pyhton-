age=int(input("enter the age : "))
if age < 18:
    print("you can't vote ")
elif age >18 and age<80:
    print("you can vote")
else:
    print("you can't vote sorry!!!!")