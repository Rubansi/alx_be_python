num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
operand = input ("Choose the operation (+,-,*,/): ")

if operand == "+":
    result = num1 + num2
    print(f"The result is {result}")
elif operand == "-":
    result = num1 - num2
    print(f"The result is {result}")
elif operand == "*":
    result = num1 * num2
    print(f"The result is {result}")
elif operand == "/":
    result = num1 / num2
    print(f"The result is {result}")

else:
    print("No division by Zero")