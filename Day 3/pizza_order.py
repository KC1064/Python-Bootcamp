print("Thank you for choosing Python Pizza Deliveries!")
size = input() # What size pizza do you want? S, M, or L
add_pepperoni = input() # Do you want pepperoni? Y or N
extra_cheese = input() # Do you want extra cheese? Y or N
# 🚨 Don't change the code above 👆
# Write your code below this line 👇
#Based on a user's order, work out their final bill.
#Small pizza (S): $15
#Medium pizza (M): $20
#Large pizza (L): $25
# Add pepperoni for small pizza (Y or N): +$2
# Add pepperoni for medium or large pizza (Y or N): +$3
# Add extra cheese for any size pizza (Y or N): +$1
if size== "L" and add_pepperoni== "Y" :
    bill=25+3
elif size== "M" and add_pepperoni== "Y":
    bill=20+3
else:
    bill=15+2

    if extra_cheese=="Y":
        bill+=1
    else:
        bill+=0
print(f"Your final bill is {bill}.")