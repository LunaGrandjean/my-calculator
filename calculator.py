print("Welcome to the calculator")

choice = int(input("What operation do you want to perform?\n1. Sum\n2. Real Division\n3. Subtraction\n4. Power\n"))

if choice == 1:
    a = int(input("Enter the first number: "))
    b = int(input("Enter the second number: "))
    print("Result:", sum(a, b))
elif choice == 2:
    a = int(input("Enter the numerator: "))
    b = int(input("Enter the denominator: "))
    print("Result:", realDivi(a, b))
