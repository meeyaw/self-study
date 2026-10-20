# This is a simple age calculator using python

from datetime import date

# dob --> Date of Birth
dob = date.fromisoformat(input("Enter Date of Birth (YYYY-MM-DD): "))
today = date.today()

years = today.year - dob.year
months = today.month - dob.month
days = today.day - dob.day

if days < 0 :
    months -= 1
    days += 30

if months < 0 :
    years -= 1
    months += 12

print(f"Your Age: {years} years, {months} months, {days} days")
input("Please hit ENTER key to exit ...")
