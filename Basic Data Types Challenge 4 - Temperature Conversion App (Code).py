import math

print("Welcome to the Right Triangle Solver App\n")

Side_1 = float(input("What is the first side of the triangle: "))
Side_2 = float(input("What is the second side of the triangle: "))

Hyp = math.sqrt(Side_1**2 + Side_2**2)
Area = 0.5 * Side_1 * Side_2

print(f"For a triangle with sides of {Side_1} and {Side_2}, the hypotenuse is {Hyp:.3f}\nand the area is {Area:.3f}")
