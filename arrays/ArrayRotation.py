#This program rotates the given array.
#It rotates in both directions: left and right

import sys as system

def LeftRotate(array,places):
    length = len(array)
    if places > length:
        print(places,"Left Rotation cannot possible here")
        system.exit(0)

    for turn in range(places):
        for i in range(length-1):
            array[i],array[i+1] = array[i+1],array[i]
##END

def RightRotate(array,places):
    length = len(array)
    if places > length:
        print(places,"Right Rotation cannot possible here")
        system.exit(0)

    # n place RightRotation is similar to (length - n) places of LeftRotation.
    LeftRotate(array,(length-places))
##END

if __name__ == "__main__":
    array = [11,22,33,44,55,66,77,88]
     
    print("Given Array :",array)
    print("Which Rotation do you want to perform :")
    print("1..For Left Rotation")
    print("2..For Right Rotation")

    rotation = int(input())
    places = int(input("How many places do you want to rotate :"))

    #places = 3
    #RightRotate(array,places)
    #print(array)

    if rotation == 1:
        LeftRotate(array,places)
        print("Array after Left Rotation :",array)
        #[44,55,66,77,88,11,22,33]

    elif rotation == 2:
        RightRotate(array,places)
        print("Array after Right Rotation :",array)
        #[66,77,88,11,22,33,44]
    else:
        print("Try Again")
        print("Program Termination")
##END
