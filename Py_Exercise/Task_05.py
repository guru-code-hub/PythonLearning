# Factorial
def factorial(n):
    # single line to find factorial
    return 1 if (n == 1 or n == 0) else n * factorial(n - 1)


num = int(input("Enter number to find factorial: "))
print("Factorial of", num, "is", factorial(num))

# fact = 1
#
# if fact == 0 or fact == 1:
#     print("Factorial of {fact}", fact)
#     else fact * fact()
