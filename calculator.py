def get_number_input(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid input. Please enter a number.")

def get_operation():
    valid_operations = {'+', '-', '*', '/'}
    while True:
        op = input("Choose operation (+, -, *, /): ").strip()
        if op in valid_operations:
            return op
        print("Invalid operation. Please choose from +, -, *, /")

def calculate(num1, num2, operation):
    if operation == '+':
        return num1 + num2
    elif operation == '-':
        return num1 - num2
    elif operation == '*':
        return num1 * num2
    elif operation == '/':
        if num2 == 0:
            raise ValueError("Cannot divide by zero!")
        return num1 / num2

def main():
    print("--- SIMPLE CALCULATOR ---")
    num1 = get_number_input("Enter first number: ")
    num2 = get_number_input("Enter second number: ")
    operation = get_operation()
    try:
        result = calculate(num1, num2, operation)
        print(f"\nResult: {num1} {operation} {num2} = {result}")
    except ValueError as e:
        print(f"\nError: {e}")

if __name__ == "__main__":
    main()
