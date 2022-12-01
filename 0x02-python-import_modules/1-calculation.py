#!/usr/bin/python3
if __name__ == "__main__":
    from calculator_1 import add, sub, mul, div
    a = 10
    b = 5
    addition = add(10, 5)
    print("{} + {} = {}".format(a, b, add(a, b)))

    minus = sub(10, 5)
    print("{} - {} = {}".format(a, b, sub(a, b)))

    subtraction = mul(10, 5)
    print("{} * {} = {}".format(a, b, mul(a, b)))

    division = div(10, 5)
    print("{} / {} = {}".format(a, b, div(a, b)))
