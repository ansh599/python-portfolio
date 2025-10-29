import time
dob = int(input("enter the date of birth"))
from datetime import datetime, timedelta
now = datetime.now()
print("Enter your date of birth (YYYY-MM-DD):")
dob_input = input()
birthday = datetime.strptime(dob_input)
difference = now - birthday
age_in_years = difference.days // 365

print(f"You are {age_in_years} years old.")
