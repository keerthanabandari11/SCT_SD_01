print("Temperature Converter")

print("1. Celsius to Fahrenheit")
print("2. Fahrenheit to Celsius")
print("3. Celsius to Kelvin")
print("4. Kelvin to Celsius")

choice = int(input("Enter your choice: "))

if choice == 1:
    c = float(input("Enter temperature in Celsius: "))
    f = (9/5) * c + 32
    print("Temperature in Fahrenheit:", f)

elif choice == 2:
    f = float(input("Enter temperature in Fahrenheit: "))
    c = (5/9) * (f - 32)
    print("Temperature in Celsius:", c)

elif choice == 3:
    c = float(input("Enter temperature in Celsius: "))
    k = c + 273.15
    print("Temperature in Kelvin:", k)

elif choice == 4:
    k = float(input("Enter temperature in Kelvin: "))
    c = k - 273.15
    print("Temperature in Celsius:", c)

else:
    print("Invalid choice")