#Name:DeekshithR,USN:1RUA25BCA0026

a = float(input("Enter first number: "))
b = float(input("Enter second number: "))
c = float(input("Enter third number: "))
match True:
    case _ if a >= b and a >= c:
        maximum = a
    case _ if b >= a and b >= c:
        maximum = b
    case _:
        maximum = c
match True:
    case _ if a <= b and a <= c:
        minimum = a
    case _ if b <= a and b <= c:
        minimum = b
    case _:
        minimum = c
print("Maximum number:", maximum)
print("Minimum number:", minimum )
