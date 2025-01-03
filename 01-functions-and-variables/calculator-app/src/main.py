def get_numbers():
    num1 = input("Enter num1: ");
    num2 = input("Enter num2: ");
    num1 = int(num1);
    num2 = int(num2);
    return num1, num2;

def get_operator():
    operator = input("Enter operator [+, -, *, /, %]: ");
    if operator in ['+', '-', '*', '/', '%']:
        return operator;
    else:
        print("please provide valid operator");
        return get_operator();

def calculate(num1, num2, operator):
    if operator == '+':
        return num1 + num2
    elif operator == '-':
        return num1 - num2
    elif operator == '*':
        return num1 * num2
    elif operator == '/':
        if num2 == 0:
            return "Error: Division by zero is not allowed"
        return num1 / num2
    elif operator == '%':
        return num1 % num2

def main():
    print("calculator app")
    num1, num2 = get_numbers();
    operator = get_operator();
    result = calculate(num1, num2, operator);
    print(f"The result of {num1} {operator} {num2} is: {result}")


if __name__ == "__main__":
    main()
