age = input()
# 🚨 Don't change the code above 👆
# Write your code below this line 👇
number_weeks_in_year = 52
total_weeks_in_ninety_years = number_weeks_in_year*90
age_in_weeks = int(age) * number_weeks_in_year
your_number_of_weeks_until_ninety_years = total_weeks_in_ninety_years - age_in_weeks
print(f"You have {your_number_of_weeks_until_ninety_years} weeks left.")