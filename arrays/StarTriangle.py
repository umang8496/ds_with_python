# This program takes an integer input (n) from the user &
# displays the "PascalTriangle" upto n number of lines.

def pT(n):
    # n is number of lines.
    array = []

    # set values for pascal triangle
    for i in range(n):
        array.append([])
        pos = (n * 2 // 2) - i
        for j in range(1, ((n * 2) - pos) + 1):
            if (pos == j):
                array[i].append
            else:
                print(" ", end="")
                array[i].append(0)

    # Display the Pascal Triangle
    for i in range(n):
        pos = (n * 2 // 2) - i
        for j in range(1, ((n * 2) - pos) + 1):
            if (pos == j):
                print("1", end="")
                pos = pos + 2
            else:
                print(" ", end="")
                array[i].append(0)
        print()

print("Welcome to StarTriangle")
n = int(input("enter the number of rows"))
pT(n)