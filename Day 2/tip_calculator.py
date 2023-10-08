#If the bill was $150.00, split between 5 people, with 12% tip. 

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

#Write your code below this line 👇
bill=float(input("Enter the bill: "))
num_of_persons=int(input("Enter the number of persons: "))
tip=(bill/num_of_persons)*1.12
rounded_tip=round(tip,2)
print(f"Each of you need to pay {rounded_tip}")