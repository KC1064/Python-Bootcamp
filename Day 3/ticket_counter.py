#Write a code to enter their height and age
#if height is grater than or equal to 120cm they can ride else they cant
#also if there is age 18 or above charge 12 dollor if less charge 7$
height=int(input("Enter your height in cm: "))
age=int(input("Enter your age: "))
bill = 0
if height >= 120:
    print("You can ride the rollercoaster")
    if age >= 18:
        bill=12
        print("Adult ticket: 12$")
    else:
        bill=7
        print("Adult ticket: 7$")
    want_photo=input("Do you want photos: Y or N")
    if (want_photo=='Y'):
        bill+=3
        print(f"Total bill to be paid {bill}")
    else:
        bill+=0
        print(f"Total bill to be paid {bill}")
    
else:
    print("You cannot ride the rollercoaster.")
