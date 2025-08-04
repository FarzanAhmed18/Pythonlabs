print("Welcome to the Temperature Conversion App\n")

Farenheit = float(input("What is the given temperature in degrees Fahrenheit:"))

Celsius = (Farenheit - 32) * 5/9

Kelvin = (Farenheit - 32) * 5/9 + 273.15

print("What do you want to convert it to?")
print("1. Celsius\n2. Kelvin")
Choice = input()

if Choice == "1":
    print(f"{Farenheit} degrees Fahrenheit is {Celsius:.4f} degrees Celsius")
elif Choice == "2":
    print(f"{Farenheit} degrees Fahrenheit is {Kelvin:.4f} degrees Kelvin")
else:
    print("Invalid option. Please choose 1 or 2.")
