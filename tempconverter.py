#Name:DeekshithR,USN:1RUA25BCA0026
temp = float(input("Enter temperature value: "))

print("Choose conversion:")
print("1. Celsius to Fahrenheit")
print("2. Fahrenheit to Celsius")

choice = int(input("Enter choice (1 or 2): "))

match choice:
    case 1:
        fahrenheit = (temp * 9/5) + 32
        print("Temperature in Fahrenheit:", fahrenheit)

    case 2:
        celsius = (temp - 32) * 5/9
        print("Temperature in Celsius:", celsius)

    case _:
        print("Invalid choice")
