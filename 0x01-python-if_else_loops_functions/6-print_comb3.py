for x in range(3, 4):
    for y in range(x + 1, 10):
        print("{:d}{:d}". format(x, y), end=', ')
print("{:d}{:d}". format(x + 1, y))
