#!/usr/bin/python3
if __name__ == "__main__":
    a, operator, b, = input('Enter calculation').split()
    a = int(a)
    b = int(b)

    if operator == "+":
        print("{} + {} = {}".format(a, b, add(a, b)))
    elif operator == "-":
        print("{} - {} = {}".format(a, b, sub(a, b)))
    elif operator == "*":
        print("{} * {} = {}".format(a, b, mul(a, b)))
    elif operator == "/":
        print("{} / {} = {}".format(a, b, div(a, b)))

    else:
        print("Unknown operator.Available operators: +, -, * and /")
