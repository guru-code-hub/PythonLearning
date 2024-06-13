# 2. Triangle Classifier:
# Write a program that classifies a triangle based on its side lengths.
# Given three input values representing the lengths of the sides,
# determine if the triangle is equilateral (all sides are equal),
# isosceles (exactly two sides are equal),
# or scalene (no sides are equal).
# Use an if-else statement to classify the triangle.
# 3 Input
# side 1, side 2 and side 3
# output - Eq, Iso, Scalene -
# Eq. = side 1 == side 2 = side 3

side_1 = int(input("Enter degree for side 1 : "))
side_2 = int(input("Enter degree for side 2 : "))
side_3 = int(input("Enter degree for side 3 : "))

if side_1 == side_2 and side_2 == side_3:
    print("Equilateral triangle")
elif side_1 == side_2 or side_2 == side_3 or side_1 == side_3:
    print("Isosceles triangle")
else:
    print("Scalane triangle")
