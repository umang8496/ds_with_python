# An array containing positive elements is given.
# ‘A’ and ‘B’ are two numbers defining a range.
# Write a function to check if the array contains all elements
# in the given range.

# Input : arr[] = {1 4 5 2 7 8 3}
#            A : 2, B : 5
# Output : Yes
#
# Input : arr[] = {1 4 5 2 7 8 3}
#           A : 2, B : 6
# Output : No

import random as rd

def ArrayWithinRange(array,l=0,u=0):
    length = len(array)
    for i in range(length):
        if(array[i] < l or array[i] > u):
            return False
    return True
# END

if __name__ == "__main__":
    array = [rd.randint(1,50) for x in range(10)]
    lower = rd.randint(1,50)
    upper = rd.randint(1,50)

    status = ArrayWithinRange(array,lower,upper)

    print("Array :",array)
    print("lower :",lower)
    print("upper :", upper)

    if status == True:
        print("Array is within the specified range.")
    else:
        print("Array is not within the specified range.")
    # END
# END