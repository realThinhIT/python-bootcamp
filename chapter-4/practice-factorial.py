"""
CALCULATE FACTORIAL
"""

print("CALCULATE FACTORIAL")

number = int(input("x! => x = "));
result = 1;

for i in range(number):
    currentIterator = i + 1;
    result *= currentIterator;

print(str(number) + "! =", result);