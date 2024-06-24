# Right Triangle Star Pattern

limit = int(input("Enter the limit : "))
# limit1 = limit
for i in range(0, limit):
    for j in range(0, i + 1):
        # print("*", end="")
        print("*", end=" ")
    print()

for i in range(limit + 1, 0, -1):
    for j in range(0, i - 1):     # here, we are declaring the for loop to print the pattern
        print("*", end=" ")
    print()
