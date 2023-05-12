#!/usr/bin/python3

if __name__ == "__main__":
    """Handle basic arithmetic operations."""
    from calculator_1 import add, sub, mul, div
    import sys

    try:
        a = int(sys.argv[1])
        op = sys.argv[2]
        b = int(sys.argv[3])
    except (ValueError, IndexError):
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)

    ops = {"+": add, "-": sub, "*": mul, "/": div}
    if op not in ops:
        print("Unknown operator. Available operators: +, -, * and /")
        sys.exit(1)

    result = ops[op](a, b)
    print(f"{a} {op} {b} = {result}")
