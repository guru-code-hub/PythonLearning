# Leap Year Checker:
# Create a program that determines whether a given year is a leap year.
# A leap year is divisible by 4, but not by 100 unless it is also divisible by 400.
# Use an if-else statement to make this determination.
# Input = 2024
# Output = Leap year

number1 = int(input("Enter a year : "))

leap_yr = number1 % 4

# print(leap_yr)

if leap_yr == 0:
    print("This is leap year")
else:
    print("Not a leap year")
