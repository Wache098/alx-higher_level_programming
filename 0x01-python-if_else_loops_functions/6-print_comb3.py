#!/usr/bin/python3
for i in range(10):
    for j in range(i+1, 10):
        print("{:02d}, {:02d}".format(i, j), end="")
        if i != 9 or j != 8:
            print(", ", end="")
        else:
            print()
