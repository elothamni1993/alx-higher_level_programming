from calculator_1 import add, sub, mul, div

def main():
    user_input = input("Enter your calculation (e.g., '3 + 5'): ")

    # Extract a, operator, and b from user_input
    a = ""
    operator = ""
    b = ""
    stage = 1  # 1 for reading a, 2 for reading operator, 3 for reading b

    for char in user_input:
        if char.isdigit():
            if stage == 1:
                a += char
            elif stage == 3:
                b += char
        elif char in ['+', '-', '*', '/']:
            if stage == 1:
                stage = 2
                operator = char
            else:
                raise ValueError("Invalid input format.")
        elif char == ' ':
            continue
        else:
            raise ValueError("Invalid character in input.")

    if not a or not operator or not b:
        raise ValueError("Usage: <a> <operator> <b>")

    a = int(a)
    b = int(b)

    if operator == "+":
        result = add(a, b)
    elif operator == "-":
        result = sub(a, b)
    elif operator == "*":
        result = mul(a, b)
    elif operator == "/":
        if b == 0:
            raise ValueError("Error: division by zero")
        result = div(a, b)
    else:
        raise ValueError("Unknown operator. Available operators: +, -, * and /")

    print("{} {} {} = {}".format(a, operator, b, result))

if __name__ == "__main__":
    try:
        main()
    except ValueError as e:
        print(e)

