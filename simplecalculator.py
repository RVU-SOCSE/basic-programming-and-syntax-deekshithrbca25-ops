#Name:DeekshithR,USN:1RUA25BCA0026
a = float(input("Enter first number: "))
b = float(input("Enter second number: "))

print("Choose operation (+, -, *, /)")
op = input("Enter operation: ")

match op:
    case "+":
        print("Result:", a + b)

    case "-":
        print("Result:", a - b)

    case "*":
        print("Result:", a * b)

    case "/":
        print("Result:", a / b)

    case _:
        print("Invalid operation")
