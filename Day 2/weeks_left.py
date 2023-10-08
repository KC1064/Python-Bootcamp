age = input("Enter your age: ")
# 🚨 Don't change the code above 👆
# Write your code below this line 👇
age_in_int=int(age)
years_left=90-age_in_int
weeks_left=years_left*52
print(f"You have {weeks_left} weeks left.")