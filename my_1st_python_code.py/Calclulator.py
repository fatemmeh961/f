print("Welcome to the calculator!")

while True:
    
    print("\nChoose an operation:")
    print("a. Press + for addition")
    print("b. Press - for subtraction")
    print("c. Press * for multiplication")
    print("d. Press / for division")
    print("e. Press q to quit the calculator")

    
    choice = input("Enter your choice (+, -, *, /, q): ")

    if choice == 'q':
        print("Goodbye! Thanks for using the calculator.")
        break

   
    if choice in ['+', '-', '*', '/']:
        try:
            num1 = float(input("Enter the first number: "))
            num2 = float(input("Enter the second number: "))

            if choice == '+':
                result = num1 + num2
                print("Result:", result)
            elif choice == '-':
                result = num1 - num2
                print("Result:", result)
            elif choice == '*':
                result = num1 * num2
                print("Result:", result)
            elif choice == '/':
                if num2 == 0:
                    print("Error: Cannot divide by zero.")
                else:
                    result = num1 / num2
                    print("Result:", result)
        except ValueError:
            print("Invalid input. Please enter numeric values.")
    else:
        print("Invalid option. Please choose +, -, *, /, or q.")
