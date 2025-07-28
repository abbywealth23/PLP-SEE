# A calculator that determines if a year is a leap year 
# Ask a user to enter a year

new_year = int(input("Enter the year: "))

if new_year % 4 == 0: 
    print(new_year.upper(), "is a leap year")
else:
    print(new_year, "is not a leap year")

