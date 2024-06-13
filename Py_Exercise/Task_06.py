# Fibonacci series
fab_num = int(input("Enter number to find Fibonacci series: "))
numb_1 = 0
numb_2 = 1
numb_3 = 0
print("Fibonacci Series:", numb_1, numb_2, end=" ")
for i in range(2, fab_num):
    numb_3 = numb_1 + numb_2
    numb_1 = numb_2
    numb_2 = numb_3
    print(numb_3, end=" ")