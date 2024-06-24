# Functions

def fun_with_default_val(name="Gururaj"):
    print(name)


def calculate():
    print(10 + 9)


calculate()
fun_with_default_val("raj")


def print_name(name, age):
    print("Hi", name, age)


print_name("GURURAJ .A.V", 42)


def sum_of_two_num(a, b):
    return a + b


a = int(input("Enter value of a: "))
b = int(input("Enter value of b: "))

result = sum_of_two_num(a, b)
print("Sum of two number is:", result)
