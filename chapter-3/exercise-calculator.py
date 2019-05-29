"""
CALCULATOR PROGRAM
"""

print("CALCULATOR PROGRAM")

firstNumber = int(input("Input a = "));
operator = input("Please choose your operator (+, -, *, /): ");
secondNumber = int(input("Input b = "));

result = None
if operator == '+':
    result = firstNumber + secondNumber
elif operator == '-':
    result = firstNumber - secondNumber
elif operator == '*':
    result = firstNumber * secondNumber
elif operator == '/':
    result = firstNumber / secondNumber
else:
    print("Invalid operator!")

if result is not None:
    print("Result:", firstNumber, operator, secondNumber, "=", result);