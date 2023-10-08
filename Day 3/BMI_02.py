# Enter your height in meters e.g., 1.55
height = float(input())
# Enter your weight in kilograms e.g., 72
weight = int(input())
# 🚨 Don't change the code above 👆

#Write your code below this line 👇Under 18.5 they are underweight
#Over 18.5 but below 25 they have a normal weight
#Equal to or over 25 but below 30 they are slightly overweight
#Equal to or over 30 but below 35 they are obese
#Equal to or over 35 they are clinically obese.

bmi=(weight)/(height**2)
bmi_int=float(bmi)

if bmi_int < 18.5:
    print(f"Your BMI is {bmi}, you are underweight.")
elif bmi_int>= 18.5 and bmi_int<25:
    print(f"Your BMI is {bmi}, you are normal weight.")
elif bmi_int>= 25 and bmi_int < 30:
    print(f"Your BMI is {bmi}, you are slightly overweight.")
elif bmi_int>= 30 and bmi_int < 35:
    print(f"Your BMI is {bmi}, you are obese.")
else:
    print (f"Your BMI is {bmi}, you are clinically obese")



