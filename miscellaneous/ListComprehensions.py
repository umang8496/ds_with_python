# Let's learn about list comprehensions! 
# You are given three integers X, Y and Z representing the dimensions of a cuboid along with an integer N.
# You have to print a list of all possible coordinates given by (1,j,k) on a 3D grid
# where the sum of is not equal to N. Here, 

# Input Format
# Four integers X, Y, Z and N each on four separate lines, respectively.

# Constraints
# Print the list in lexicographic increasing order.

def ListComprehensions():
    x = int(input())
    y = int(input())
    z = int(input())
    N = int(input())

    return_list = []

    for i in range(0,x+1):
        for j in range(0, y+1):
            for k in range(0, z+1):
                if (i+j+k != N):
                    return_list.append([i,j,k])

    print(return_list)
## END

if __name__ == "__main__":
    ListComprehensions()
## END