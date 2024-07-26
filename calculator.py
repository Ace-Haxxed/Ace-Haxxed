def calculator():
    while True:
        num1 = float(input("What is the 1st number? "))
        operator = input("What is the operator? (Multiplication, Division, Subtraction, or Addition): ")
        num2 = float(input("2nd number? "))

        if operator == 'Multiplication':
            print(num1 * num2)
        elif operator == 'Division':
            if num2 != 0:
                print(num1 / num2)
            else:
                print("No dividing by 0!")
        elif operator == 'Subtraction':
            print(num1 - num2)
        elif operator == 'Addition':
            print(num1 + num2)
        else:
            print("Invalid operator")


calculator()
